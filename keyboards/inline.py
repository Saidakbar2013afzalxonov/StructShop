from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

def mahsulotlar(products):
        keyboard=[]

        for product in products:
            keyboard.append([InlineKeyboardButton(text=f"{product['name'] } ({product['price']} $)",callback_data=f"product_{product['id']}")])
    
        return InlineKeyboardMarkup(inline_keyboard=keyboard)
