from aiogram import Router,F
from aiogram.types import Message,CallbackQuery
from keyboards.reply import location
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup
from keyboards.inline import crypto
from keyboards.reply import asosiy_menyu

router=Router()

class SotibOlish(StatesGroup):
    location=State()
    crypto_money=State()
    number_of_card=State()

@router.callback_query(F.data.startswith("sotib_olish:"))
async def sotib_olish(call:CallbackQuery,state:FSMContext):
    await call.message.answer(f"Mahsulotni yetkazib berishimiz uchun manzilingizni yuboring:",reply_markup=location())
    await state.set_state(SotibOlish.location)
    await call.answer("")

@router.message(SotibOlish.location)
async def sotib_olish_location(msg:Message,state:FSMContext):
    if not msg.location:
        return await msg.answer("Iltimos, tugma orqali lokatsiya yuboring!")
    await state.update_data(latitude=msg.location.latitude, longitude=msg.location.longitude)
    await msg.answer("Siz to'lov qilmoqchi bo'lgan pul turini tanlang: ",reply_markup=crypto())
    await state.set_state(SotibOlish.crypto_money)

# datalar=["crypto_UZS","crypto_RUB","crypto_USD","crypto_KZT","crypto_JPY","crypto_EUR"]

@router.callback_query(F.data.startswith("crypto_"))
async def sotib_olish2(call:CallbackQuery,state:FSMContext):
    crypto1 = call.data.split("_")[1]
    await state.update_data(crypto=crypto1)
    await call.message.answer("Karta raqamingizni kiriting: ")
    await state.set_state(SotibOlish.number_of_card)

@router.message(SotibOlish.number_of_card)
async def sotib_olish3(msg:Message,state:FSMContext):
    await state.update_data(number_of_card=msg.text)
    if len(msg.text) == 16 or len(msg.text) == 19:
        await msg.answer("Mahsulot muvaffaqiyatli sotib olindi! Kerakli miqdordagi pul ham yechib olindi!",reply_markup=asosiy_menyu())
        data = await state.get_data()
        await state.clear()
    else:
        await msg.answer("Iltimos haqiqiy karta raqamingizni kiriting!")
        