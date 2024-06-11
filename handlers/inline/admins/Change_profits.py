from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from database.db_working import AdminWorking

router = Router()
router.message.filter(
    F.chat.type == "private"
)


@router.message(Command('profit'))
async def change_user_role(message: Message):
    if await AdminWorking.check_admin(message.from_user.id) == 'admin' or await AdminWorking.check_admin(
            message.from_user.id) == 'support':
        text = message.text.split(' ')

        await AdminWorking.profit_update(username=text[1][1:], profit=text[2])
