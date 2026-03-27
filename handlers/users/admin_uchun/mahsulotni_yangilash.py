from aiogram import F,Router
from aiogram.types import Message,CallbackQuery
from filters.adminfilter import RoleFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup,State
from keyboards.inline import mahsulotni_tahrirlash



class Mahsulot_yangilash(StatesGroup):
    product_id=State()
    name=State()
    price=State()
    description=State()

router=Router()

@router.callback_query(F.data.startswith("product_"),RoleFilter("admin"))
async def control(call:CallbackQuery):
    product_id=int(call.data.split("_")[1])
    await call.message.answer("Mahsulotni yangilaysizmi yoki o'chirasizmi?: ",reply_markup=mahsulotni_tahrirlash(product_id))
    await call.answer()

@router.callback_query(F.data.startswith("delete_product_"))
async def delete(call:CallbackQuery,db):
    product_id=int(call.data.split("_")[2])
    await db.mahsulotni_ochirish(product_id)
    await call.message.answer("Mahsulot o'chirildi!")
    await call.answer()


@router.callback_query(F.data.startswith("edit_product_"))
async def update(call:CallbackQuery,state:FSMContext):
    product_id=int(call.data.split("_")[2])
    await state.set_state(Mahsulot_yangilash.product_id)
    await state.update_data(product_id=product_id)
    await call.message.answer("Mahsulotni nomini kiriting: ")
    await state.set_state(Mahsulot_yangilash.name)

@router.message(Mahsulot_yangilash.name)
async def update_product(msg:Message,state:FSMContext):
    await state.update_data(name=msg.text)
    await msg.answer("Mahsulot narxini kiriting: ")
    await state.set_state(Mahsulot_yangilash.price)

@router.message(Mahsulot_yangilash.price)
async def update_product(msg:Message,state:FSMContext):
    await state.update_data(price=int(msg.text))
    await msg.answer("Mahsulot haqida yozing: ")
    await state.set_state(Mahsulot_yangilash.description)

@router.message(Mahsulot_yangilash.description)
async def update_product(msg:Message,state:FSMContext,db):
    await state.update_data(description=msg.text)
    data= await state.get_data()
    await db.mahsulotni_yangilash(data["product_id"],data["name"],data["price"],data["description"])
    await msg.answer("Mahsulot yangilandi!")
    await state.clear()