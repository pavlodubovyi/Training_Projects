import asyncio
import random
from concurrent.futures import ProcessPoolExecutor


async def ping(signal):
    print(f"Pinging {signal}")


async def ping_worker():
    while True:
        await asyncio.sleep(1)
        await ping(random.randint(1, 100))


def cpu_bound_operation(counter: int):
    init = counter
    while counter > 0:
        counter -= 1
    print(f"Operation completed: {init}")
    return init


async def main():
    loop = asyncio.get_running_loop()
    task = loop.create_task(ping_worker())

    with ProcessPoolExecutor(2) as executor:
        futures = [
            loop.run_in_executor(executor, cpu_bound_operation, counter)
            for counter in [100_000_000, 120_000_000, 150_000_000]
        ]
        res = await asyncio.gather(*futures)
        task.cancel()
        return res


if __name__ == "__main__":
    result = asyncio.run(main())
    print(result)
