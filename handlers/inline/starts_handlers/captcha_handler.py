import random

from aiogram import F

from aiogram import Router
from aiogram.types import CallbackQuery

from keyboards.inline.application_in import application_post
from keyboards.inline.captcha import capthas_emojis

router = Router()
router.message.filter(
    F.chat.type == "private"
)
emoji = ['😀️', '😃️', '😁️', '😎️', '🐶️', '🐱️', '🦎️', '🍏️', '🧂️', '🍳️', '🍆️', '🍉️', '⚽️', '🎱️', '🚲️', '🚗️', '⏰️', '🛢️',
         '💡️', '🧱️', '❤️', '🧡️', '💙️', '🖤️', '❌️', '🚭️', '💤️', '🍺️', '🍪️', '🍾️']


@router.callback_query(F.data.contains('emoji'))
async def message_with_text(call: CallbackQuery):
    await call.answer()
    data = call.data.split('.')
    await call.answer()
    if data[1].strip() == data[2].strip():
        await call.message.answer('Вы прошли каптчу')

        await call.message.answer('📝Подайте заявку на вступление', reply_markup=application_post())
    else:
        str = []
        random.shuffle(emoji)
        rn = random.randint(0, 4)

        for i in range(0, 5):
            str.append(emoji[i])

        await call.message.answer(f"Пройдите капчу\n{str[rn]}", reply_markup=capthas_emojis(str, rn).as_markup())
