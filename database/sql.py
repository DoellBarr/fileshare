from databases import Database

from config import DB_URI


class DB:
    def __init__(self):
        self.db = Database(DB_URI)

    async def connect(self):
        return await self.connect()

    async def init(self):
        await self.db.execute(
            """create table if not exists broadcast
            (
                user_id integer,
                user_name text
            )"""
        )
        return

    async def get_user(self, user_id: int):
        x = await self.db.fetch_one("select * from broadcast where user_id = :user_id", {"user_id": user_id})
        return bool(x)

    async def add_user(self, user_id: int, user_name: str):
        if not await self.get_user(user_id):
            await self.db.execute("insert into broadcast values (:user_id, :user_name)", {
                "user_id": user_id,
                "user_name": user_name
            })

    async def query_msg(self):
        return await self.db.fetch_all(
            "select user_id from broadcast"
        )

    async def full_userbase(self):
        users = await self.db.fetch_all("select * from broadcast")
        return users

    async def disconnect(self):
        return await self.db.disconnect()


db = DB()
