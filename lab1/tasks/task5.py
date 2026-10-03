import asyncio


async def first_func():
    print("Первая функция: принт 1")
    await asyncio.sleep(1)

    print("Первая функция: принт 2")
    await asyncio.sleep(4)

    print("Первая функция: принт 3")


async def second_func():
    print("Вторая функция: принт 1")
    await asyncio.sleep(3)

    print("Вторая функция: принт 2")
    await asyncio.sleep(1)

    print("Вторая функция: принт 3")
    await asyncio.sleep(1)

    print("Вторая функция: принт 4")


async def main():
    await asyncio.gather(
        first_func(),
        second_func()
    )


asyncio.run(main())