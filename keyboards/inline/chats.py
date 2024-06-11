import random

from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from config import chat_ids


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
    kb.row(InlineKeyboardButton(
        text="Проверить подписку",
        callback_data='check_subscribe')
    )
    return kb
