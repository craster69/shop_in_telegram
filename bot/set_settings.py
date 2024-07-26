from environs import Env
from aiogram import Bot, Dispatcher
from src.handlers.message.start import app as start

env = Env()

env.read_env("../config.env")

token = env.str('TOKEN')

admin_id = env.int('ADMIN_ID')


async def main():

    bot: Bot = Bot(token=token)

    dp: Dispatcher = Dispatcher()

    dp.include_routers(start)

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)

    except Exception as ex:
        print(f"[ERROR]: {ex}")

    finally:
        await bot.session.close()