import asyncio
import time
import uuid
from typing import Dict
import functools


def get_time() -> int:
    """ current unix time in milliseconds """
    return int(time.time() * 1000)


def log_processing_time(func):
    @functools.wraps(func)
    async def wrapper(self, item: Dict, spider: str, *args, **kwargs) -> Dict:
        start_time = get_time()
        result = await func(self, item, spider)
        end_time = get_time()
        processed_time = end_time - start_time
        self.logger.info("processed", id=item['_id'], time_ms=processed_time, pipeline=self.name, started_at=start_time, finished_at=end_time)
        return result
    return wrapper


def get_uuid() -> str:
    return uuid.uuid4().hex


async def cancel_task(t: asyncio.Task) -> None:
    if t and not t.done():
        t.cancel()
        try:
            await t
        except asyncio.CancelledError:
            pass


def get_real_time(monotonic_time: float) -> float:
    """"
    convert monotonic time to real world time, milliseconds
    """
    real_time = monotonic_time + (time.time() - asyncio.get_running_loop().time())
    return int(real_time * 1000)