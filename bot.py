from aiogram import Bot,Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
from config import config
from database.db import Database
from handlers.start import router as start_router
from states.register import router as register_router
from handlers.users.profile import router as profile_router
from handlers.mahsulotlar.products import router as products_router
from handlers.admin_panel import router as admin_router
from handlers.foydalanuvchilar import router as foydalanuvchilar
from handlers.users.admin_uchun.mahsulotni_yangilash import router as mahsulotni_yangilash
from handlers.Orqaga.Orqaga import router as orqaga_router
from handlers.mahsulot_sotib_olish.sotib_olish import router as sotib_olish_router
from handlers.mahsulot_sotib_olish.davomi_sotib_olish import router as davomi_sotib_olish_router


async def main():
    bot=Bot(token=config.BOT_TOKEN)
    dp=Dispatcher(storage=MemoryStorage())


    db=Database()
    await db.connection()
    dp["db"]=db

    dp.include_router(start_router)
    dp.include_router(register_router)
    dp.include_router(profile_router)
    dp.include_router(products_router)
    dp.include_router(admin_router)
    dp.include_router(foydalanuvchilar)
    dp.include_router(mahsulotni_yangilash)
    dp.include_router(orqaga_router)
    dp.include_router(sotib_olish_router)
    dp.include_router(davomi_sotib_olish_router)
    

    print("Bot is starting...")
    await dp.start_polling(bot)
    

if __name__=="__main__":
    asyncio.run(main())