from aiogram import Router,F
from aiogram.types import Message,CallbackQuery
from filters.adminfilter import RoleFilter
from keyboards.inline import savatcha_kb

router=Router()

@router.callback_query(F.data.startswith("savatga_qoshish:"),RoleFilter("user"))
async def savatcha(call:CallbackQuery,db):
    product_id=int(call.data.split(":")[1])
    user_id=await db.get_user_id(call.from_user.id)
    await db.add_product_to_cart(user_id,product_id)
    await call.answer("Mahsulot savatga qo'shildi")


@router.message(F.text=="Mening savatim")
async def savatcha(msg:Message,db):
    user_id= await db.get_user_id(msg.from_user.id)
    products=await db.get_cart_products(user_id)
    await msg.answer("Mahsulotlar ro'yxati: ",reply_markup=savatcha_kb(products))