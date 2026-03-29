from aiogram.types import Message
from aiogram import Router,F
from aiogram.filters import BaseFilter,CommandStart
from filters.adminfilter import RoleFilter
from keyboards.reply import admin_panel

router=Router()

@router.message(F.text=="Admin panel",RoleFilter('admin'))
async def admin(msg:Message):
    await msg.answer("Assalomu alaykum admin xush kelibsiz!",reply_markup=admin_panel())

@router.message(F.text=="Admin panel",RoleFilter('user'))
async def user(msg:Message):
    await msg.answer("Sizni adminlik huquqingiz yo'q")