from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def capthas_emojis(emojis, rn):
    kb = InlineKeyboardBuilder()
    for i in emojis:
        kb.add(InlineKeyboardButton(
            text=i,
            callback_data=f"emoji.{i}.{emojis[rn]}"
        )
        )

    return kb
