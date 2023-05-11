import disnake
import aiosqlite




class UserDataBase:
    def __init__(self):
        self.name = 'dbs/users.db'


    async def create_table(self):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = '''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY key,
                name TEXT,
                warns INTEGER,
                roles TEXT
            );'''
            await cursor.execute(query)
            await db.commit()

    
    async def add_warns(self, user: disnake.Member, value = 1):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = 'UPDATE users SET warns = warns +? WHERE id = ?'
            await cursor.execute(query, (value,user.id))
            await db.commit()

    async def remove_warns(self, user: disnake.Member, value = 1):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = 'UPDATE users SET warns = warns -? WHERE id = ?'
            await cursor.execute(query, (value,user.id))
            await db.commit()



    async def add_user(self, user: disnake.Member):
        async with aiosqlite.connect(self.name) as db:
            if not await self.get_user(user):
                cursor = await db.cursor()
                query = 'INSERT INTO users (id, name, warns, roles) VALUES (?, ?, ?, ?);'
                await cursor.execute(query, (user.id, user.name, 0, ''))
                await db.commit()


    async def get_user(self, user: disnake.Member):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = 'SELECT * FROM users WHERE id = ?'
            await cursor.execute(query, (user.id,))
            return await cursor.fetchone()


    async def add_roles(self, user: disnake.Member, roles):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = 'UPDATE users SET roles = ? WHERE id = ?'
            await cursor.execute(query, (roles,user.id))
            await db.commit()


    async def remove_roles(self, user: disnake.Member):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = 'UPDATE users SET roles = ? WHERE id = ?'
            await cursor.execute(query, (1,user.id))
            await db.commit()