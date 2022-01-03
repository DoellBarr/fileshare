import asyncio

from database.sql import db


async def main():
    await db.init()
    await db.add_user(123, "abc")
    print(await db.query_msg())
    await db.disconnect()


asyncio.get_event_loop().run_until_complete(main())
