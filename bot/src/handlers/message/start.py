from aiogram.types import Message
from aiogram.filters.command import CommandStart
from aiogram import Router, F, Bot
import requests
from environs import Env
from typing import NamedTuple
from datetime import datetime
import os, sys

sys.path.append(os.getcwd())

from db.requests import *

app = Router()

env = Env()

env.read_env('config.env')

token = env.str('TOKEN')

admin_id = env.int('ADMIN_ID')

class UserData(NamedTuple):
    user_id: int
    user_name: str
    file_id: str
    file_path: str
    date: datetime


async def user_data(message: Message) -> UserData:

    try:
        photos = await message.from_user.get_profile_photos()

        file_id: str = photos.photos[0][-1].file_id

        file_path: str = requests.get(f'https://api.telegram.org/bot{token}/getFile?file_id={file_id}').json()['result']['file_path']

    except:
        file_id = None

        file_path = None
    
    finally:
        user_id: int = message.from_user.id

        user_name: str = message.from_user.full_name

        date: datetime = message.date

    return UserData(
        user_id=user_id,
        file_id=file_id,
        file_path=file_path,
        user_name=user_name,
        date=date 
    )


@app.message(CommandStart())
async def start(message: Message):
    
    data = await user_data(message)
    
    await add_user(data)

    user = await get_user_by_id(data.user_id)

    print(user.file_id)

    await message.answer(f'<blockquote>{message.text}</blockquote>\nПривет, {data.user_name}')


@app.startup()
async def start_work(bot: Bot):
    await bot.send_message(
        admin_id, "Начало сессии"
    )

@app.shutdown()
async def start_work(bot: Bot):
    await bot.send_message(
        chat_id=admin_id, text="Завершении сессии"
    )


