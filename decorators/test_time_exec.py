import functools
import time


def test_time_exec(iters=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            total = 0
            for _ in range(iters):
                start = time.perf_counter()
                value = func(*args, **kwargs)
                end = time.perf_counter()
                total += end - start
            print(f'Average time of {func.__name__}: {round(total / iters, 4)} sec.')
            return value
        return wrapper
    return decorator
