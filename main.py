import asyncio
from aiogram import Bot, Dispatcher

from database import create_db
from handlers import user_handler, admin_handler, captcha_handler
from handlers.admins import change_role, Change_profits, User_bans

bot = Bot(token="5772775343:AAGB3u8LMPtuQYMgVWV3DikEgmXVYq2IXdA")


async def main():
    dp = Dispatcher()

    dp.include_router(user_handler.router)
    dp.include_router(captcha_handler.router)
    dp.include_router(admin_handler.router)
    dp.include_routers(change_role.router, Change_profits.router, User_bans.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    create_db()
    asyncio.run(main())
