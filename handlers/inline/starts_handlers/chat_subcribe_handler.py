import datetime

from aiogram import F

from aiogram import Router
from aiogram.types import CallbackQuery

from config import chat_ids
from database.db_working import UserWorking
from keyboards.inline.chats import chats_for_subs
from keyboards.user_kb import main_user_profile

router = Router()
router.message.filter(
    F.chat.type == "private"
)


@router.callback_query(F.data == 'check_subscribe')
async def check_subscribes(call: CallbackQuery):
    await call.answer()
    check = True

    for chat_id in chat_ids:
        print(chat_id)
        chat_member = await call.bot.get_chat_member(chat_id, call.message.from_user.id)
        if chat_member.status.split('.')[0] == 'left':
            await call.message.answer('Вы не подписались на все каналы!!!', reply_markup=chats_for_subs())
            check = False

    if check:
        await call.message.delete()
        await call.message.answer('Добро пожаловать!', reply_markup=main_user_profile())
        await UserWorking.add_user(username=call.from_user.username, user_id=call.from_user.id,
                                   time=datetime.date.today())
