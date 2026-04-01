from aiogram import Router,F
from aiogram.types import Message,CallbackQuery
from keyboards.inline import savatcha_kb

router=Router()

# @router.callback_query(F.data.startswith("remove_product_"))
# async def remove(call:CallbackQuery,db):
#     product_id=int(call.data.split("_")[2])
#     user_id= await db.get_user_id(call.from_user.id)
#     await db.remove_one_product(product_id, user_id)
#     products=db.get_or_create_cart(user_id)
#     await call.message.answer("Mahsulot savatdan o‘chirildi!",reply_markup=savatcha_kb(products))

@router.callback_query(F.data.startswith("remove_product_"))
async def remove_from_cart(call:CallbackQuery,db):
    user_id= await db.get_user_id(call.from_user.id)
    product_id= int(call.data.split("_")[2])
    await db.remove_one_product(user_id,product_id)
    products=await db.get_cart_products(user_id)
    await call.message.answer("Mahsulotlar ro'yxati: ",reply_markup=savatcha_kb(products))
    await call.answer()