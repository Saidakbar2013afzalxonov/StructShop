from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router,F
from keyboards.reply import register
from keyboards.reply import asosiy_menyu

router=Router()


@router.message(CommandStart())
async def start_handler(msg:Message,db):
    if await db.is_user_exists(msg.from_user.id):
        await msg.answer("Assalomu Alaykum botga xush kelibsz!",reply_markup=asosiy_menyu())
    else:
        await msg.answer("Assalomu alaykum StructShop botiga xush kelibsiz!\nIltimos biz sizni tanib olishimiz uchun ro'yxatdan o'ting!",reply_markup=register())


        
    