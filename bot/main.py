from config import token
from aiogram import F, Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command
from asyncio import run 


async def main():

    bot: Bot = Bot(token=token)


    dp: Dispatcher = Dispatcher()


    try:
        await dp.start_polling(bot)

    except Exception as ex:
        print(f"[ERROR]: {ex}")

    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        run(main())
    
    except KeyboardInterrupt:
        print("exit...")