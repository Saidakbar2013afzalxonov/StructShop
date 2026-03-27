from aiogram.types import Message
from aiogram import Router,F
from keyboards.inline import foydalanuvchilar_kb

router=Router()


@router.message(F.text == "Foydalanuvchilar")
async def foydalanuvchilar(msg:Message,db):
    users = await db.foydalanuvchilar() 
    await msg.answer("Foydalanuvchilar ro'yxati:",reply_markup=foydalanuvchilar_kb(users))