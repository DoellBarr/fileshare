import asyncio

from pyrogram.errors import FloodWait

from sql import db


async def users_info(bot):
    user = blocked = 0
    identity = await db.query_msg()
    for ids in identity:
        name = bool()
        try:
            name = await bot.send_chat_action(int(ids[0]), "typing")
        except FloodWait as e:
            await asyncio.sleep(e.x)
        if bool(name):
            user += 1
        else:
            blocked += 1
    return user, blocked
