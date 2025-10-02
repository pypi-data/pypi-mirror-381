import asyncio
import random
from loguru import logger
from datetime import datetime, timezone, timedelta
from typing import Any, Optional, Dict, Callable




class GGSCache:
    def __init__(
        self,
        on_expire: Optional[Callable[[Any, Any], Any]] = None,
        default_ttl: float = 5.0
    ):
        # Memcache logic
        self._data: Dict[Any, Any] = {}
        self._default_ttl = default_ttl
        # Ensure on_expire is always callable (no-op by default)
        self._on_expire = on_expire if on_expire is not None else (lambda *args, **kwargs: None)

        self._tasks: Dict[Any, asyncio.Task] = {}
        self._expiry_times: Dict[Any, datetime] = {}
        self._locks: Dict[Any, asyncio.Lock] = {}

    # -----------------------
    # API fără TTL (by design)
    # -----------------------
    def set(self, key: Any, value: Any):
        """Setează o valoare permanent (fără TTL)."""
        self._data[key] = value

    def get(self, key: Any, default: Any = None):
        """
        Returnează valoarea, cu invalidare leneșă dacă a expirat.
        Dacă a expirat între timp, șterge intrarea, anulează task-ul
        și rulează on_expire în fundal.
        """
        exp = self._expiry_times.get(key)
        if exp is not None and datetime.now(timezone.utc) >= exp:
            payload = self._data.pop(key, None)
            self._expiry_times.pop(key, None)
            task = self._tasks.pop(key, None)
            if task:
                task.cancel()
                # drenăm task-ul fără a bloca
                try:
                    asyncio.get_running_loop().create_task(self._drain_task(task))
                except RuntimeError:
                    # nu există loop rulând (ex: apel sync în teardown)
                    pass
            if payload is not None:
                try:
                    res = self._on_expire(key, payload)
                    if asyncio.iscoroutine(res):
                        try:
                            asyncio.get_running_loop().create_task(res)
                        except RuntimeError:
                            pass
                except Exception:
                    logger.exception("Exception in on_expire during lazy get-expire for key %r", key)
            return default
        return self._data.get(key, default)

    def delete(self, key: Any):
        """Șterge intrarea și oprește task-ul de expirare (dacă există)."""
        self._data.pop(key, None)
        task = self._tasks.pop(key, None)
        if task:
            task.cancel()
            try:
                asyncio.get_running_loop().create_task(self._drain_task(task))
            except RuntimeError:
                pass
        self._expiry_times.pop(key, None)

    # -----------------------
    # API cu programare/TTL
    # -----------------------
    async def set_with_ttl(self, key: Any, value: Any, ttl: Optional[float] = None):
        """
        Setează valoarea cu un TTL. Protejat cu lock per cheie
        pentru a evita condiții de cursă când mai multe corutine
        setează aceeași cheie aproape simultan.
        """
        lock = self._locks.setdefault(key, asyncio.Lock())
        async with lock:
            await self._set_with_ttl_unlocked(key, value, ttl)

    async def _set_with_ttl_unlocked(self, key: Any, value: Any, ttl: Optional[float]):
        self._data[key] = value
        ttl = ttl if ttl is not None else self._default_ttl
        deadline = datetime.now(timezone.utc) + timedelta(seconds=ttl)
        self._expiry_times[key] = deadline

        # înlocuiește task-ul existent (dacă e)
        old = self._tasks.pop(key, None)
        if old:
            old.cancel()
            try:
                asyncio.get_running_loop().create_task(self._drain_task(old))
            except RuntimeError:
                pass

        # pornește un task care verifică deadline-ul real (rezistent la lag)
        self._tasks[key] = asyncio.create_task(self._expire_later(key))

    async def _expire_later(self, key: Any):
        """
        Așteaptă până la deadline-ul curent din _expiry_times.
        Re-verifică deadline-ul după sleep (rezistent la event-loop lag).
        """
        try:
            while True:
                deadline = self._expiry_times.get(key)
                if deadline is None:
                    return  # șters manual sau resetat
                now = datetime.now(timezone.utc)
                remaining = (deadline - now).total_seconds()
                if remaining > 0:
                    await asyncio.sleep(remaining)
                    # după sleep re-verificăm; dacă deadline-ul a fost mutat,
                    # bucla va continua până când ajungem la termenul final
                    continue

                payload = self._data.pop(key, None)
                if payload is not None:
                    try:
                        res = self._on_expire(key, payload)
                        if asyncio.iscoroutine(res):
                            await res
                    except Exception:
                        logger.exception("Exception in on_expire for key %r", key)
                break
        except asyncio.CancelledError:
            # task anulat explicit (delete/clear/reprogramare)
            pass
        finally:
            self._tasks.pop(key, None)
            self._expiry_times.pop(key, None)

    async def set_in_timeline(self, key: Any, value: Any, delay: float, jitter: float = 0.0):
        """
        Programează expirarea relativ la momentul apelului.
        Ultimul apel câștigă (anulează programarea anterioară).
        """
        jitter_val = random.uniform(-jitter, jitter) if jitter > 0 else 0.0
        delay = max(0.0, delay + jitter_val)
        await self.set_with_ttl(key, value, delay)

    async def schedule_after_last(self, key: Any, value: Any, interval: float, jitter: float = 0.0):
        """
        Împinge expirarea DUPĂ ultima expirare programată (dacă există),
        altfel o setează relativ la acum. Ideal pentru „lanțuri”.
        """
        lock = self._locks.setdefault(key, asyncio.Lock())
        async with lock:
            now = datetime.now(timezone.utc)
            expiry = self._expiry_times.get(key)
            if expiry is None or expiry < now:
                delay = 0.0
            else:
                delay = (expiry - now).total_seconds()
            jitter_val = random.uniform(-jitter, jitter) if jitter > 0 else 0.0
            delay += max(0.0, interval + jitter_val)
            await self._set_with_ttl_unlocked(key, value, delay)

    # -----------------------
    # Curățare / Shutdown
    # -----------------------
    def clear(self):
        """
        Șterge toate intrările și anulează task-urile.
        Drenarea task-urilor se face în fundal (dacă există event loop).
        """
        for task in self._tasks.values():
            task.cancel()
            try:
                asyncio.get_running_loop().create_task(self._drain_task(task))
            except RuntimeError:
                pass
        self._data.clear()
        self._tasks.clear()
        self._expiry_times.clear()
        self._locks.clear()

    async def aclose(self):
        """
        Închidere curată (apel recomandat la shutdown-ul aplicației).
        Așteaptă toate task-urile de expirare să se termine.
        """
        tasks = list(self._tasks.values())
        for t in tasks:
            t.cancel()
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)
        self._data.clear()
        self._tasks.clear()
        self._expiry_times.clear()
        self._locks.clear()

    # -----------------------
    # Utilitare interne
    # -----------------------
    async def _drain_task(self, task: asyncio.Task):
        """Așteaptă un task anulat, ignorând erorile de anulare."""
        try:
            await task
        except asyncio.CancelledError:
            pass
        except Exception:
            logger.exception("Background task raised after cancel")
