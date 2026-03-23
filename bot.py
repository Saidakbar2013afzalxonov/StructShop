from aiogram import Bot,Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
from config import config
from Database.db import Database


async def main():
    bot=Bot(token=config.BOT_TOKEN)
    dp=Dispatcher(storage=MemoryStorage())

    db=Database()
    await db.connection()
    dp["db"]=db

    print("Bot is starting...")
    await dp.start_polling(bot)
    

if __name__=="__main__":
    asyncio.run(main())