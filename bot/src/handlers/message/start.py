from aiogram.types import Message
from aiogram.filters.command import CommandStart
from aiogram import Router


app = Router()


@app.message(CommandStart())
async def start(message: Message):
    await message.answer('тестовое сообщение!')