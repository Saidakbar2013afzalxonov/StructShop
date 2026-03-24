from aiogram import Router,F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from keyboards.reply import asosiy_menyu
from aiogram.fsm.state import StatesGroup,State

class RegisterState(StatesGroup):
    name=State()
    surename=State()
    age=State()
    phone_number=State()

router=Router()

@router.message(F.text=="Register")
async def register(msg:Message,state:FSMContext,db):
    await msg.answer("Ro'yxatdan o'tish uchun ismingizni kiriting: ")
    await state.set_state(RegisterState.name)

@router.message(RegisterState.name)
async def register(msg:Message,state:FSMContext):
    await state.update_data(name=msg.text)
    await msg.answer("Familyangizni kiriting: ")
    await state.set_state(RegisterState.surename)


@router.message(RegisterState.surename)
async def register(msg:Message,state:FSMContext):
    await state.update_data(surename=msg.text)
    await msg.answer("Yoshingizni kiriting: ")
    await state.set_state(RegisterState.age)

@router.message(RegisterState.age)
async def register(msg:Message,state:FSMContext):
    await state.update_data(age=msg.text)
    await msg.answer("Telefon raqamingizni kiriting: ")
    await state.set_state(RegisterState.phone_number)

@router.message(RegisterState.phone_number)
async def register(msg:Message,state:FSMContext,db):
    await state.update_data(phone_number=msg.text)
    data=await state.get_data()
    await msg.answer(text=f" Malumotlaringiz: \nIsmingiz: {data['name']}\nFamilyangiz: {data['surename']}\nYoshingiz: {data['age']}\nTelefon raqamingiz: {data['phone_number']}",reply_markup=asosiy_menyu())
    await db.add_user(int(msg.from_user.id),data["name"],data["surename"],int(data["age"]),data["phone_number"])
    await msg.answer("Malumotlarigiz muvaffaqiyatli saqlandi")
    await state.clear()
    