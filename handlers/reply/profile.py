from aiogram.types import Message
from aiogram import F
from aiogram import Router

from database.db_working import ApplicationWorking, UserWorking
from keyboards.inline.main_profile.Profile_kb import main_profile

router = Router()
router.message.filter(
    F.chat.type == "private"
)


@router.message(F.text == "👤Личный Кабинет")
async def user_profile(message: Message):
    app = await ApplicationWorking.get_app_by_id(message.from_user.id)
    print(message.from_user.id)
    print(app)
    user = await UserWorking.get_user(message.from_user.id)
    text = f"""Профиль:
    ├─ID: {message.from_user.id}
    ├─Юзернейм: {message.from_user.username}
    ├─Баланс: {user.profit} RUB.
    ├─Получено с шопа: {None}RUB.
    ├─В боте с: {user.date}
    └─Логов, готовых к выгрузке: {None}
    """
    await message.answer(text=text, reply_markup=main_profile())


@router.message(F.text.lower() == "🔱Топ пользователей")
async def tops_users(message: Message):
    await message.reply("Отличный выбор!")


@router.message(F.text.lower() == "💬Чаты")
async def users_chats(message: Message):
    await message.reply("Отличный выбор!")


@router.message(F.text.lower() == "📦Получить билд")
async def gaves_build(message: Message):
    await message.reply("Отличный выбор!")
