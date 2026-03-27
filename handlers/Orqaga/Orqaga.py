from aiogram.types import Message
from aiogram import Router,F
from keyboards.reply import asosiy_menyu

router=Router()

@router.message(F.text=="Orqaga")
async def orqaga(msg:Message):
    await msg.answer("Boshlang'ich menyuga o'tildi!",reply_markup=asosiy_menyu())