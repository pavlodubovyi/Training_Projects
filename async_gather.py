import asyncio
from faker import Faker
from time import time

fake = Faker("uk-UA")


async def async_user_from_db(uuid: int):
    await asyncio.sleep(0.5)
    return {"id": uuid, "username": fake.user_name(), "email": fake.email()}


async def main():
    users = []
    for i in range(1, 6):
        users.append(async_user_from_db(i))
    """
        попередній рядок = наступні 2:
        task = asyncio.create_task(async_user_from_db(i))
        users.append(task)
    """
    result = await asyncio.gather(*users)
    return result


if __name__ == "__main__":
    print("Starting ASYNC...")
    start = time()
    our_users = asyncio.run(main())
    print(our_users)
    print(f"Result: {time() - start}")
