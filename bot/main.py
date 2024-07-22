from config import token
from aiogram import Bot, Dispatcher
from asyncio import run 
from src.handlers.message.start import app as start

async def main():

    bot: Bot = Bot(token=token)


    dp: Dispatcher = Dispatcher()

    dp.include_routers(start)


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