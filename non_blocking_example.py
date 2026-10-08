import asyncio


async def task():
    print("Task started")

    await asyncio.sleep(3)

    print("Task finished")


asyncio.run(task())