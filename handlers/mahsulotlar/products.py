from aiogram import F,Router
from aiogram.types import Message
from keyboards.inline import mahsulotlar

router=Router()

@router.message(F.text=="Mahsulotlar")
async def products(msg:Message,db):
    products=await db.mahsulot_olish()
    await msg.answer(f"Mahsulotlar ro'yxati: ",reply_markup=mahsulotlar(products))