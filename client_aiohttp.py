from datetime import datetime, timedelta

import aiohttp
import asyncio
import sys

# два наступні використовую, бо інакше вилазить помилка SSLCertVerificationError
import ssl
import certifi


class HttpError(Exception):
    pass


async def request(url: str):
    # обробляю сертифікат
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
                    raise HttpError(f"Error status: {response.status} for {url}")
        except (aiohttp.ClientConnectorError, aiohttp.InvalidURL) as error:
            raise HttpError(f"Connection error: {url}", str(error))


async def main(num_of_days):
    if not (1 <= num_of_days <= 10):
        raise ValueError("Number of days must be between 1 and 10")

    formatted_data = []
    for i in range(num_of_days):
        datum = datetime.now() - timedelta(days=i)
        delta = datum.strftime("%d.%m.%Y")
        try:
            the_response = await request(
                f"https://api.privatbank.ua/p24api/exchange_rates?json&date={delta}"
            )
            formatted_data.extend(format_currency_data(the_response, delta))
        except HttpError as err:
            raise HttpError(f"Error: {err}")
    return formatted_data


# функція, яка виділяє тільки потрібні нам EUR та USD і форматує відповідно до умови ДЗ
def format_currency_data(data, days_num):
    formatted_data = []
    entry = {days_num: {}}

    for currency_info in data["exchangeRate"]:
        currency_code = currency_info["currency"]
        if currency_code in ["USD", "EUR"]:
            sale_rate = currency_info.get("saleRate", currency_info["saleRateNB"])
            purchase_rate = currency_info.get(
                "purchaseRate", currency_info["purchaseRateNB"]
            )

            entry[days_num][currency_code] = {
                "sale": sale_rate,
                "purchase": purchase_rate,
            }

    formatted_data.append(entry)
    return formatted_data


if __name__ == "__main__":
    try:
        days = int(sys.argv[1])
    except (IndexError, ValueError):
        print("Please provide a valid number of days as a command-line argument.")
        sys.exit(1)

    try:
        response = asyncio.run(main(days))
        print(response)
    except HttpError as e:
        print(f"Error: {e}")
        sys.exit(1)
