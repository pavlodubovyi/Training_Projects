from time import time
from functools import wraps


def async_timer(name: str = None):
    if name:
        print(f"Executing async function: {name}")

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


def sync_timer(name: str = None):
    if name:
        print(f"Executing async function: {name}")

    def inner(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            start = time()
            try:
                return func(*args, **kwargs)
            finally:
                print(time() - start)

        return wrapped

    return inner
