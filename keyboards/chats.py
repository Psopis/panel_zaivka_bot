import random

from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def chats_for_subs():
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(
        text="Чат",
        url='https://t.me/testPsopi')
    )
    kb.add(InlineKeyboardButton(
        text="Чат",
        url='https://t.me/testPsopi')
    )
    kb.add(InlineKeyboardButton(
        text="Чат",
        url='https://t.me/testPsopi')
    )
    return kb
