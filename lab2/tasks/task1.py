import asyncio


async def mes(delay, message):
    await asyncio.sleep(delay)
    print(message)

async def main():
    await mes(2, "Привет!")


if __name__ == "__main__":
    asyncio.run(main())