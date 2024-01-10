from time import time
from functools import wraps


def async_time(name: str = None):
    if name:
        print(f"Your decorator has a name: {name}")

    def inner(func):
        @wraps(func)
        async def wrapped(*args, **kwargs):
            start = time()
            try:
                return await func(*args, **kwargs)
            finally:
                print(time() - start)

        return wrapped

    return inner
