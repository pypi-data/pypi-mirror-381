import json
import time
import math
import inspect
import tracemalloc

class Colors:
    YELLOW    = '\033[93m'
    RED       = '\033[91m'
    WHITE     = '\033[0m'

class PyProfyler:
    def sizeformat(self, bytes):
        units = ["B", "KB", "MB", "GB"]
        if bytes == 0:
            return "0.0B"
        i = int(math.floor(math.log(bytes, 1024)))
        return f"{bytes / (1024 ** i):.2f}{units[i]}"
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.profiled = False
        self.profile = {}
        self.memsamples = []
    def trace_mem(self):
        current, _ = tracemalloc.get_traced_memory()
        self.memsamples.append(current)
    def profileit(self, start_time):
        if not self.memsamples:  # safeguard
            self.memsamples.append(0)
        mem_mean = sum(self.memsamples) / len(self.memsamples)
        mem_peak = max(self.memsamples)
        self.profile = {
            'func': self.func.__name__,
            'mem_mean': self.sizeformat(mem_mean),
            'mem_peak': self.sizeformat(mem_peak),
            'perfc': time.perf_counter() - start_time
        }
        self.profiled = True
        tracemalloc.stop()
    def __call__(self, *args, **kwargs):
        call_args = args if args else self.args
        call_kwargs = kwargs if kwargs else self.kwargs
        tracemalloc.start()
        start_time = time.perf_counter()
        self.memsamples = []
        if inspect.isgeneratorfunction(self.func):
            def gen_wrapper():
                for item in self.func(*call_args, **call_kwargs):
                    self.trace_mem()
                    yield item
                self.profileit(start_time)
            return gen_wrapper()
        elif inspect.isasyncgenfunction(self.func):
            async def async_gen_wrapper():
                async for item in self.func(*call_args, **call_kwargs):
                    self.trace_mem()
                    yield item
                self.profileit(start_time)
            return async_gen_wrapper()
        elif inspect.iscoroutinefunction(self.func):
            async def coro_wrapper():
                result = await self.func(*call_args, **call_kwargs)
                self.trace_mem()
                self.profileit(start_time)
                return result
            return coro_wrapper()
        else:
            result = self.func(*call_args, **call_kwargs)
            self.trace_mem()
            self.profileit(start_time)
            return result
    def __str__(self):
        if not self.profiled:
            return f"{Colors.YELLOW}{self.func.__name__} hasn't been executed yet.{Colors.WHITE}"
        return json.dumps(self.profile, indent=4)
