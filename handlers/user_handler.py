import datetime
import random

from aiogram import Router, F

from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import config
from database.db_working import UserWorking, AdminWorking
from keyboards.inline.captcha import capthas_emojis

router = Router()
router.message.filter(
    F.chat.type == "private"
)

chat_ids = [-1001608843060, ]
emoji = ['😀️', '😃️', '😁️', '😎️', '🐶️', '🐱️', '🦎️', '🍏️', '🧂️', '🍳️', '🍆️', '🍉️', '⚽️', '🎱️', '🚲️', '🚗️',
         '⏰️', '🛢️',
         '💡️', '🧱️', '❤️', '🧡️', '💙️', '🖤️', '❌️', '🚭️', '💤️', '🍺️', '🍪️', '🍾️']


@router.message(Command("start"))
async def user_start(message: Message, state: FSMContext):
    is_admin = False
    if await UserWorking.check_user(message.from_user.id):
        pass
    else:

        for i in config.admins:
            if i == message.from_user.id:
                await AdminWorking.add_admin(username=message.from_user.username, user_id=message.from_user.id, time=datetime.date.today())
                is_admin = True
        if is_admin:
            await message.answer(f"Здравствуте {message.from_user.username}")
        else:
            str = []
            random.shuffle(emoji)
            rn = random.randint(0, 4)

            for i in range(0, 5):
                str.append(emoji[i])

            await message.answer(f"Пройдите капчу\n{str[rn]}", reply_markup=capthas_emojis(str, rn).as_markup())
