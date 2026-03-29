from aiogram.types import Message,CallbackQuery
from aiogram import Router,F
from keyboards.inline import foydalanuvchilar_kb,user_role
from filters.adminfilter import RoleFilter

router=Router()


@router.message(F.text == "Foydalanuvchilar")
async def foydalanuvchilar(msg:Message,db):
    users = await db.foydalanuvchilar() 
    await msg.answer("Foydalanuvchilar ro'yxati:",reply_markup=foydalanuvchilar_kb(users))

@router.callback_query(F.data.startswith("user_"))
async def users(call:CallbackQuery,db):
    user_id= int(call.data.split("_")[1])
    await call.message.answer("Foydalanuvchi rolini tanlang:",reply_markup=user_role(user_id))
    await call.answer()

@router.callback_query(F.data.startswith("foydalanuvchi_"),RoleFilter('admin'))
async def user(call:CallbackQuery,db): 
    _,role,user_id=call.data.split("_")
    user_id=int(user_id)
    await db.rolni_yangilash(user_id,role)
    await call.message.answer("Role o'zgartirildi!")
    await call.answer()

