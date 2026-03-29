from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

def mahsulotlar(products):
        keyboard=[]

        for product in products:
            keyboard.append([InlineKeyboardButton(text=f"{product['name'] } ({product['price']} $)",callback_data=f"product_{product['id']}")])
    
        return InlineKeyboardMarkup(inline_keyboard=keyboard)


def foydalanuvchi_rollari(user_id):
      return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="admin",callback_data=str(f"changeto_admin_{user_id}")),InlineKeyboardButton(text="user",callback_data=str(f"changeto_user_{user_id}"))]
        ]
    )

def foydalanuvchilar_kb(users):
    keyboards=[]

    for user in users:
        keyboards.append([InlineKeyboardButton(text=f"{user['name']} {user['surename']}({user['role']})",callback_data=f"user_{user['id']}")])
    
    return InlineKeyboardMarkup(inline_keyboard=keyboards)

def mahsulotni_tahrirlash(product_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Yangilash",callback_data=f"edit_product_{product_id}"),InlineKeyboardButton(text="O'chirish",callback_data=f"delete_product_{product_id}")]
        ]
    )

def sotib_olish_kb(product_id ):
     return InlineKeyboardMarkup(
          inline_keyboard=[
               [InlineKeyboardButton(text="Sotib olish",callback_data=f"sotib_olish:{product_id}"),InlineKeyboardButton(text="Savatga qo'shish",callback_data=f"savatga_qoshish:{product_id}")]
          ]
     )

def crypto():
     return InlineKeyboardMarkup(
          inline_keyboard=[
               [InlineKeyboardButton(text="UZS",callback_data="crypto_UZS"),InlineKeyboardButton(text="USD",callback_data="crypto_USD")],
               [InlineKeyboardButton(text="RUB",callback_data="crypto_RUB"),InlineKeyboardButton(text="EUR",callback_data="crypto_EUR")],
               [InlineKeyboardButton(text="KZT",callback_data="crypto_KZT"),InlineKeyboardButton(text="JPY",callback_data="crypto_JPY")]
          ]
     )


def savatcha_kb(products):
    keyboard=[]

    for product in products:
        keyboard.append([InlineKeyboardButton(text=f"{product['name'] } ({product['price']} $)",callback_data='kerak_emas'),InlineKeyboardButton(text="Mahsulotni savatdan o'chirish",callback_data=f"remove_product_{product['id']}")])
    
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def user_role(user_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="admin",callback_data=f'foydalanuvchi_admin_{user_id}'),InlineKeyboardButton(text="user",callback_data=f'foydalanuvchi_user_{user_id}')]
        ]
    )