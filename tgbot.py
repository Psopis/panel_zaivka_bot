import asyncio
from aiogram import Bot, Dispatcher

from config import TOKEN
from database.setup import init_db, close_db
from handlers import user_handler, admin_handler
from handlers.inline.starts_handlers import captcha_handler, application_handler, chat_subcribe_handler
from handlers.inline.admins import User_bans, Change_profits, change_role
from handlers.reply import profile
bot = Bot(token=TOKEN)


async def on_startup():
    await init_db()


async def run_main():
    dp = Dispatcher()

    dp.include_router(user_handler.router)
    dp.include_router(captcha_handler.router)
    dp.include_router(admin_handler.router)
    dp.include_router(application_handler.router)
    dp.include_router(chat_subcribe_handler.router)
    dp.include_router(profile.router)
    dp.include_routers(change_role.router, Change_profits.router, User_bans.router)
    await on_startup()
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(run_main())
    except (KeyboardInterrupt, SystemExit):
        asyncio.run(close_db())
        print("Бот был выключен!")
