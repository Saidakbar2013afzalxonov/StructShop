from aiogram.types import Message
from aiogram.filters import CommandStart

@router.message(CommandStart())
async def start_handler(msg:Message,db):
    await msg.answer("Assalomu alykum StructShop botiga xush kelibsiz!")