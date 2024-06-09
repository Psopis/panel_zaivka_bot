from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from database import check_admin, get_id_from_name

router = Router()


@router.message(Command('ban'))
async def change_user_role(message: Message):
    if check_admin(message.from_user.id)[0] == 'admin' or check_admin(message.from_user.id)[0] == 'support':
        text = message.text.split(' ')
        # Проблема с получение username через user_id через базу данных какая то ошибка котелок не варит уже
        # get_id_from_name(text[1][1:]) эта функция принимает username и кароч должна возвращать user_id из бд
        print(get_id_from_name(text[1][1:]))
        # await message.bot.ban_chat_member(user_id=, chat_id=message.chat.id)
