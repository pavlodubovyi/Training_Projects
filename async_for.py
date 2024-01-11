import asyncio
from typing import AsyncIterator, Coroutine, Any
from faker import Faker
from timing import async_timer

fake = Faker("uk-UA")  # en-GB


async def get_user_from_db(uuid: int):
    await asyncio.sleep(0.5)
    return {"id": uuid, "username": fake.user_name(), "email": fake.email()}


async def get_users(uuids: list[int]) -> AsyncIterator:
    for el in uuids:
        yield get_user_from_db(el)


@async_timer("-- main --")
async def main(users: AsyncIterator):
    users_ = []
    async for user in users:
        users_.append(user)
    result = await asyncio.gather(*users_)
    return result


if __name__ == "__main__":
    r = asyncio.run(main(get_users([1, 2, 3])))
    print(r)
