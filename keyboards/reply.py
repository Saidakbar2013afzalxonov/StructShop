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
            [KeyboardButton(text="Profile"),KeyboardButton(text="Buyurtmalar tarixi")],
            [KeyboardButton(text="Admin panel")]
        ],
        resize_keyboard=True
    )

def admin_panel():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Mahsulotlar")],
            [KeyboardButton(text="Mahsulot qo'shish"),KeyboardButton(text="Foydalanuvchilar")],
            [KeyboardButton(text="Sotilgan mahsulotlar"),KeyboardButton(text="Orqaga")]   
        ],
        resize_keyboard=True
    )

def location():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Manzilni yuborish",request_location=True)]
        ],
        resize_keyboard=True
    )