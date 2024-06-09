from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from database import check_admin
from keyboards.admins.admins import admins_panel
from main import bot

router = Router()


class AdminsPanelBtn(StatesGroup):
    role = State()
    ban = State()
    profit = State()


@router.message(Command('adm'))
async def admin_start(message: Message):
    print(check_admin(message.from_user.id)[0])
    if check_admin(message.from_user.id)[0] == 'admin':

        await message.answer(f"Привестую Вас {message.from_user.username}\n"
                             f"Смена роли: /role <Роль> <username>\n"
                             f"Бан: /ban <username>\n"
                             f"Смена профита: /profit <сумма> <username>")
