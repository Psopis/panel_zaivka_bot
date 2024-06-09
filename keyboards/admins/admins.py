import random

from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def admins_panel():
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(
        text="Обновить роль",
        callback_data='Update_role')
    )
    kb.add(InlineKeyboardButton(
        text="Забанить",
        callback_data='User_ban')
    )
    kb.add(InlineKeyboardButton(
        text="Изменить профит",
        callback_data='Change_profit')
    )
    return kb

def role_change():
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(
        text="Админ",
        callback_data='admin')
    )
    kb.add(InlineKeyboardButton(
        text="Воркер",
        callback_data='Worker')
    )
    kb.add(InlineKeyboardButton(
        text="Саппорт",
        callback_data='support')
    )
    return kb