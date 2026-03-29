from aiogram import Router,F
from aiogram.filters import BaseFilter
from filters.adminfilter import RoleFilter
from aiogram.types import Message,CallbackQuery
from keyboards.inline import sotib_olish_kb

router=Router()

@router.callback_query(F.data.startswith(f"product_"),RoleFilter("user"))
async def sotib_olish1(call:CallbackQuery,db):
    product_id=int(call.data.split("_")[1])
    await call.message.answer(f"Mahsulotni sotib olasizmi yoki savatga qo'shasizmi?",reply_markup=sotib_olish_kb(product_id))
    await call.answer()