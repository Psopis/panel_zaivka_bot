from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from database import check_admin, profit_update
from keyboards.admins.admins import admins_panel, role_change

router = Router()


@router.message(Command('profit'))
async def change_user_role(message: Message):
    if check_admin(message.from_user.id)[0] == 'admin':
        text = message.text.split(' ')

        try:

            profit_update(username=text[1][1:], profit=text[2])
        except:
            await message.answer('Неправильно написана команда')