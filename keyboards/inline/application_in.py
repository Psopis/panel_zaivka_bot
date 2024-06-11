from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def application_post():
    kb = InlineKeyboardBuilder()

    kb.add(InlineKeyboardButton(
        text="Подать заявку",
        callback_data=f"application_post"
    )
    )

    return kb.as_markup()


def application_accept(user_id):
    kb = InlineKeyboardBuilder()

    kb.add(InlineKeyboardButton(
        text="✅Одобрить",
        callback_data=f"application_accepted.{user_id}"
    )
    )
    kb.add(InlineKeyboardButton(
        text="❌Отказать",
        callback_data=f"application_denial.{user_id}"
    )
    )

    return kb.as_markup()
