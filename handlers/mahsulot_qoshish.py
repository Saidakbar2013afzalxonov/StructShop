from aiogram import Router,F
from aiogram.types import Message
from filters.adminfilter import RoleFilter
from aiogram.fsm.state import State,StatesGroup
from aiogram.fsm.context import FSMContext


router=Router()

class MahsulotQoshish(StatesGroup):
    name=State()
    price=State()
    description=State()

@router.message(F.text=="Mahsulot qo'shish",RoleFilter('admin'))
async def mahsulot_qoshish(msg:Message,state:FSMContext):
    await msg.answer("Mahsulotni qo'shish uchun mahsulot nomini kiriting: ")
    await state.set_state(MahsulotQoshish.name)

@router.message(MahsulotQoshish.name)
async def add_product(msg:Message,state:FSMContext):
    await state.update_data(name=msg.text)
    # await msg.answer("Mahsulot narxini kiriting: ")
    # if msg.text==str():
    #     await msg.answer("Iltimos mahsulot nariga son kiriting!")
    # else:
    #     await state.set_state(MahsulotQoshish.price)
    await msg.answer("Mahsulot narxini kiriting:")

    if not msg.text.isdigit():
        await msg.answer("Iltimos mahsulot narxini son ko‘rinishida kiriting!")
    else:
        await state.update_data(price=int(msg.text))
        await state.set_state(MahsulotQoshish.price)
    
@router.message(MahsulotQoshish.price)
async def add_product(msg:Message,state:FSMContext):
    await state.update_data(price=int(msg.text))
    await msg.answer("Mahsulot description kiriting: ")
    await state.set_state(MahsulotQoshish.description)

@router.message(MahsulotQoshish.description)
async def add_product(msg:Message,state:FSMContext,db):
    await state.update_data(description=msg.text)
    data=await state.get_data()
    await db.mahsulot_qoshish(data["name"],data["price"],data["description"])
    await msg.answer("Mahsulot muvaffaqiyatli qo'shildi")
    await state.clear()
