import asyncio
from concurrent.futures import ThreadPoolExecutor
import requests
from requests.exceptions import InvalidSchema, MissingSchema, SSLError
from timing import async_timer, sync_timer

urls = [
    "https://github.com",
    "https://www.codewars.com",
    "https://realpython.com/",
    "https://glosbe.com/",
    "https://www.youtube.com/",
    "https://en.wikipedia.org/wiki/Wiki",
    "ws://test.com/",
    "Asdf",
]


def get_previews(url: str) -> tuple[str, str]:
    result = requests.get(url)
    return url, result.text[:25]  # show first 25 symbols


@sync_timer()
def main_sync():
    results = []
    for url in urls:
        try:
            results.append(get_previews(url))
        except (InvalidSchema, MissingSchema, SSLError) as err:
            print(err)
    return results


@async_timer()
async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor(6) as executor:
        futures = [loop.run_in_executor(executor, get_previews, url) for url in urls]
        res = await asyncio.gather(*futures, return_exceptions=True)
    return res


if __name__ == "__main__":
    print(main_sync())

    outcome: list = asyncio.run(main())
    new_outcome = []
    for el in outcome:
        if isinstance(el, Exception):
            continue
        new_outcome.append(el)
    print(new_outcome)
