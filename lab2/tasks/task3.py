import requests
import asyncio
import time


urls = [
    "https://mail.ru",
    "https://ya.ru",
    "https://google.com"
]

def norm_request():
    print("Обычные запросы:")

    start_all = time.perf_counter()

    for url in urls:
        start = time.perf_counter()
        response = requests.get(url)
        end = time.perf_counter()

        print(f'{url} - время: {end - start} сек')

    print(f'Общее время: {time.perf_counter() - start_all} сек')


async def async_request(url):
    start = time.perf_counter()
    resp = await asyncio.to_thread(requests.get, url)
    end = time.perf_counter()

    print(f'{url} - время: {end - start} сек')

async def asynchronous():
    print("\nАсинхронные запросы:")
    start_all = time.perf_counter()
    tasks = []

    for url in urls:
        tasks.append(async_request(url))

    await asyncio.gather(*tasks)
    print(f'Общее время: {time.perf_counter() - start_all} сек')


if __name__ == "__main__":
    norm_request()
    asyncio.run(asynchronous())

