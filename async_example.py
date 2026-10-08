import asyncio


async def say_hello():
    print("Hello")

    await asyncio.sleep(2)

    print("Welcome back")


asyncio.run(say_hello())