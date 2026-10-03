import asyncio


async def mes(delay, message):
    await asyncio.sleep(delay)
    print(message)

async def main():
    await asyncio.gather(
        mes(2, "1"),
        mes(1, "2"),
        mes(3, "3")
    )


if __name__ == "__main__":
    asyncio.run(main())
