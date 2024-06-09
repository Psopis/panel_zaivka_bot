import random

from aiogram import Router, F

from aiogram import Router
from aiogram.types import Message, CallbackQuery

from database import add_user
from keyboards.captcha import capthas_emojis

router = Router()
emoji = ['😀️', '😃️', '😁️', '😎️', '🐶️', '🐱️', '🦎️', '🍏️', '🧂️', '🍳️', '🍆️', '🍉️', '⚽️', '🎱️', '🚲️', '🚗️', '⏰️', '🛢️',
         '💡️', '🧱️', '❤️', '🧡️', '💙️', '🖤️', '❌️', '🚭️', '💤️', '🍺️', '🍪️', '🍾️']


@router.callback_query(F.data.contains('emoji'))
async def message_with_text(call: CallbackQuery):
    data = call.data.split('.')
    await call.answer()
    if data[1].strip() == data[2].strip():
        await call.message.answer('Вы прошли каптчу')
        add_user(username=call.from_user.username, user_id=call.from_user.id)
    else:
        str = []
        random.shuffle(emoji)
        rn = random.randint(0, 4)

        for i in range(0, 5):
            str.append(emoji[i])

        await call.message.answer(f"Пройдите капчу\n{str[rn]}", reply_markup=capthas_emojis(str, rn).as_markup())
