from abc import ABC, abstractmethod
import asyncio
import time
from typing import Callable, ClassVar, Dict, Type, Coroutine
from structlog import BoundLogger

from zenx.settings import Settings
from zenx.exceptions import NoBlueprintAvailable, NoSessionAvailable
from zenx.utils import get_real_time



class Schedular(ABC):
    name: ClassVar[str]
    _registry: ClassVar[Dict[str, Type["Schedular"]]] = {}
    shutdown_event = asyncio.Event()


    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, "name"):
            raise TypeError("Schedular subclass {cls.__name__} must have a 'name' attribute.")
        cls._registry[cls.name] = cls

    
    @classmethod
    def get_schedular(cls, name: str) -> Type["Schedular"]:
        if name not in cls._registry:
            raise ValueError(f"Schedular '{name}' is not registered. Available schedulars: {list(cls._registry.keys())}") 
        return cls._registry[name]


    def __init__(self, logger: BoundLogger, settings: Settings) -> None:
        self.logger = logger
        self.settings = settings


    async def open(self) -> None:
        if self.settings.END_DATETIME:
            loop = asyncio.get_running_loop()
            real_world_clock = time.time()
            monotonic_clock = loop.time()

            offset = real_world_clock - monotonic_clock
            
            end_time = self.settings.END_DATETIME.timestamp() - offset
            loop.call_at(end_time, self.shutdown_event.set)
        self.logger.debug("opened", schedular=self.name)
        
    
    async def execute_task(self, task_func: Callable[[], Coroutine]) -> None:
        loop = asyncio.get_running_loop()
        try:
            self.logger.debug("executing task", at=get_real_time(loop.time()))
            await task_func()
        except (NoSessionAvailable, NoBlueprintAvailable):
            self.logger.error("crawl failed", reason="session pool exhausted")
        except Exception:
            self.logger.exception("crawl failed", reason="unexpected")


    @abstractmethod
    async def run(self, task_func: Callable[[], Coroutine], start_time: float) -> None:
        ...


    async def close(self) -> None:
        self.logger.debug("closed", schedular=self.name)



class WorkersSchedular(Schedular):
    """
    High precision schedular.
    Each worker will run every TASK_INTERVAL_SECONDS. Overall they would be (TASK_INTERVAL_SECONDS / CONCURRENCY) apart.
    Task execution time is not taken into account. This means that if task takes longer than TASK_INTERVAL_SECONDS, next task will run immediately.
    """
    name = "workers"
    

    async def _dispatcher(self, task_func: Callable[[], Coroutine], start_time: float) -> None:
        loop = asyncio.get_running_loop()
        tick = 0
        tick_interval = self.settings.TASK_INTERVAL_SECONDS # 5

        while not self.shutdown_event.is_set():
            target_time = start_time + (tick * tick_interval) # 1698393010.0 + (0 * 5) = 1698393010.0, 1698393015.0, 1698393020.0
            delay = (target_time - loop.time()) - 0.050

            if delay:
                # wake up early to avoid delayed task execution
                self.logger.debug("sleeping", target_time=get_real_time(target_time), monotonic_clock=get_real_time(loop.time()), sleep_time=delay, should_wake_at=get_real_time(loop.time() + delay))
                await asyncio.sleep(delay)
            self.logger.debug("waked up early", target_time=get_real_time(target_time), monotonic_clock=get_real_time(loop.time()))

            while True:
                monotonic_clock = loop.time()
                if monotonic_clock >= target_time:
                    break
                await asyncio.sleep(0)
            self.logger.debug("time has come", target_time=get_real_time(target_time), monotonic_clock=get_real_time(monotonic_clock), drift=get_real_time(monotonic_clock) - get_real_time(target_time))

            await self.execute_task(task_func)

            tick += 1

    
    async def run(self, task_func: Callable[[], Coroutine], start_time: float) -> None:
        tick_interval = self.settings.TASK_INTERVAL_SECONDS / self.settings.CONCURRENCY # 5/10 = 0.5
        
        loop = asyncio.get_running_loop()
        async with asyncio.TaskGroup() as tg:
            for worker_id in range(self.settings.CONCURRENCY): # 10
                worker_start_time_on_loop = start_time + (worker_id * tick_interval) # 1698393010.0 + (0 * 0.5) , 1698393010.5, 1698393011.0
                real_world_clock = time.time()
                monotonic_clock = loop.time()
                offset = real_world_clock - monotonic_clock
                worker_start_time = worker_start_time_on_loop + offset
                self.logger.debug("scheduled", worker_id=worker_id, worker_start_time=worker_start_time)

                tg.create_task(self._dispatcher(task_func, worker_start_time_on_loop))





# class OldWorkersSchedular(Schedular):
#     """
#     Each worker will run every TASK_INTERVAL_SECONDS. Overall they would be (TASK_INTERVAL_SECONDS / CONCURRENCY) apart.
#     Task execution time is not taken into account. This means that if task takes longer than TASK_INTERVAL_SECONDS, next task will run immediately.
#     """
#     name = "old_workers"
    

#     async def _dispatcher(self, task_func: Callable[[], Coroutine], start_time: float) -> None:
#         loop = asyncio.get_running_loop()
#         tick = 0
#         tick_interval = self.settings.TASK_INTERVAL_SECONDS # 5

#         while not self.shutdown_event.is_set():
#             target_time = start_time + (tick * tick_interval) # 1698393010.0 + (0 * 5) = 1698393010.0, 1698393015.0, 1698393020.0
#             delay = target_time - loop.time()

#             if delay > 0:
#                 await asyncio.sleep(delay)

#             await self.execute_task(task_func)

#             tick += 1

    
#     async def run(self, task_func: Callable[[], Coroutine], start_time: float) -> None:
#         tick_interval = self.settings.TASK_INTERVAL_SECONDS / self.settings.CONCURRENCY # 5/10 = 0.5
        
#         async with asyncio.TaskGroup() as tg:
#             for worker_id in range(self.settings.CONCURRENCY): # 10
#                 worker_start_time = start_time + (worker_id * tick_interval) # 1698393010.0 + (0 * 0.5) , 1698393010.5, 1698393011.0
#                 tg.create_task(self._dispatcher(task_func, worker_start_time))


