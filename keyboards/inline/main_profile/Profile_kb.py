from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_profile():
    kb = InlineKeyboardBuilder()

    kb.add(InlineKeyboardButton(
        text="Выгрузить  логи",
        callback_data=f"Uploads_logs"
    )
    )
    kb.add(InlineKeyboardButton(
        text="Скрыть в топе",
        callback_data=f"Hides_in_tops"
    )
    )
    kb.add(InlineKeyboardButton(
        text="Закрыть",
        callback_data=f"Close"
    )
    )

    return kb.as_markup()
