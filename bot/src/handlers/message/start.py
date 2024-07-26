from aiogram.types import Message
from aiogram.filters.command import CommandStart
from aiogram import Router, F, Bot
import requests
from environs import Env


app = Router()

env = Env()

env.read_env('config.env')

token = env.str('TOKEN')

admin_id = env.int('ADMIN_ID')


async def user_data(message: Message):

    try:
        photos = await message.from_user.get_profile_photos()

        file_id = photos.photos[0][-1].file_id

        file_path = requests.get(f'https://api.telegram.org/bot{token}/getFile?file_id={file_id}').json()['result']['file_path']

    except:
        file_id = None

        file_path = None
    
    finally:
        user_id = message.from_user.id

        user_name = message.from_user.full_name

        date = message.date

    data = {
        'file_id' : file_id,
        'file_path' : file_path,
        'user_id' : user_id,
        'user_name' : user_name,
        'date' : date
    }

    return data


@app.message(CommandStart())
async def start(message: Message):
    
    data = await user_data(message)

    print(data)

    await message.answer('Регистрация прошла успешно!')


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