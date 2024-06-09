import random

from aiogram import Router, F

from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from database import check_user
from keyboards.captcha import capthas_emojis
from keyboards.chats import chats_for_subs
from main import bot

router = Router()
chat_ids = [-1001608843060, ]
emoji = ['😀️', '😃️', '😁️', '😎️', '🐶️', '🐱️', '🦎️', '🍏️', '🧂️', '🍳️', '🍆️', '🍉️', '⚽️', '🎱️', '🚲️', '🚗️', '⏰️', '🛢️',
         '💡️', '🧱️', '❤️', '🧡️', '💙️', '🖤️', '❌️', '🚭️', '💤️', '🍺️', '🍪️', '🍾️']


@router.message(Command("start"))
async def user_start(message: Message, state: FSMContext):

    if check_user(message.from_user.id):
        await message.answer('asd')
    else:

        check = True
        for chat_id in chat_ids:
            chat_member = await bot.get_chat_member(chat_id, message.from_user.id)
            if chat_member.status.split('.')[0] == 'left':
                check = False

        if check:
            str = []
            random.shuffle(emoji)
            rn = random.randint(0, 4)

            for i in range(0, 5):
                str.append(emoji[i])

            await message.answer(f"Пройдите капчу\n{str[rn]}", reply_markup=capthas_emojis(str, rn).as_markup())


        else:
            await message.answer("Вы должны подписаться на каналы", reply_markup=chats_for_subs().as_markup())
