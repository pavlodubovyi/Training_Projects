import asyncio


async def mygen(u: int = 10):
    """Yield powers of 2."""
    i = 0
    while i < u:
        yield 2 ** i
        i += 1
        await asyncio.sleep(0.1)

async def main():
    g = [i async for i in mygen()]
    f = [j async for j in mygen() if not (j // 3 % 5)]
    return g, f


g, f = asyncio.run(main())
# g [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
# f [1, 2, 16, 32, 256, 512]