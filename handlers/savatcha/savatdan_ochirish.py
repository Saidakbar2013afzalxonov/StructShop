from aiogram import Router,F
from aiogram.types import Message,CallbackQuery

router=Router()

@router.callback_query(F.data.startswith("remove_product_"))
async def remove(call:CallbackQuery,db):
    product_id=int(call.data.split("_")[2])
    user_id= await db.get_user_id(call.from_user.id)
    await call.message.answer(db.remove_one_product(product_id,user_id))