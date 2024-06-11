from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message


from database.db_working import AdminWorking

router = Router()
router.message.filter(
    F.chat.type == "private"
)


class AdminsPanelBtn(StatesGroup):
    role = State()
    ban = State()
    profit = State()


@router.message(Command('adm'))
async def admin_start(message: Message):

    if await AdminWorking.check_admin(message.from_user.id) == 'admin':

        await message.answer(f"Привестую Вас {message.from_user.username}\n"
                             f"Смена роли: /role <username> <Роль>\n"
                             f"Бан: /ban <username>\n"
                             f"Разбан: /unban <username>\n"
                             f"Смена профита: /profit <username> <сумма>")
