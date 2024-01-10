import asyncio
from faker import Faker
from timing import async_timer

fake = Faker("uk-UA")


async def async_user_from_db(uuid: int, future: asyncio.Future):
    await asyncio.sleep(0.5)
    future.set_result({"id": uuid, "username": fake.user_name(), "email": fake.email()})


def make_request(uuid: int) -> asyncio.Future:
    future = asyncio.Future()
    asyncio.create_task(async_user_from_db(uuid, future))
    return future


@async_timer("Future check")
async def main():
    users = []
    for i in range(1, 6):
        users.append(make_request(i))
    print([user.done() for user in users])
    result = await asyncio.gather(*users)
    print([user.done() for user in users])
    return result


if __name__ == "__main__":
    our_users = asyncio.run(main())
    print(our_users)
