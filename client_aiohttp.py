import aiohttp
import asyncio

# Додаю наступні два рядки, бо без них чомусь весь час вилазить помилка SSLCertVerificationError
import ssl
import certifi


# клас для відловлення помилок
class HttpError(Exception):
    pass


async def request(url: str):
    # додаю підключення до сертифікатів:
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    async with aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(ssl=ssl_context)
    ) as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    result = await response.json()
                    return result
                else:
                    raise HttpError(f"Error status: {resp.status} for {url}")
        except (aiohttp.ClientConnectorError, aiohttp.InvalidURL) as error:
            raise HttpError(f"Connection error: {url}", str(error))


async def main():
    try:
        res_ponse = await request(
            "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5"
        )
        return res_ponse
    except HttpError as err:
        print(err)
        return "Oops!"


if __name__ == "__main__":
    r = asyncio.run(main())
    print(r)
