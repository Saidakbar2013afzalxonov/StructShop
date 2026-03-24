from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

def register():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Register")]
        ],
        resize_keyboard=True
    )

def asosiy_menyu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Mahsulotlar"),KeyboardButton(text="Mening savatim")],
            [KeyboardButton(text="Profile"),KeyboardButton(text="Buyurtmalar tarixi")]
        ],
        resize_keyboard=True
    )