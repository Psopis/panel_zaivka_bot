from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from database.db_working import UserWorking, AdminWorking

router = Router()


@router.message(Command('ban'))
async def change_user_role(message: Message):
    if await AdminWorking.check_admin(message.from_user.id) == 'admin' or await AdminWorking.check_admin(
            message.from_user.id) == 'support':

        if message.reply_to_message:

            await message.bot.ban_chat_member(message.chat.id, user_id=message.reply_to_message.from_user.id)
            await message.delete()
        else:
            text = message.text.split(' ')
            user_id = await UserWorking.get_id_from_name(text[1][1:])
            await message.bot.ban_chat_member(message.chat.id, user_id=user_id)
            await message.delete()


@router.message(Command('unban'))
async def change_user_role(message: Message):
    if await AdminWorking.check_admin(message.from_user.id) == 'admin' or await AdminWorking.check_admin(
            message.from_user.id) == 'support':
        text = message.text.split(' ')
        if message.reply_to_message:
            await message.bot.unban_chat_member(message.chat.id, user_id=message.reply_to_message.from_user.id)
            await message.delete()
        else:
            user_id = await UserWorking.get_id_from_name(text[1][1:])
            await message.bot.unban_chat_member(message.chat.id, user_id=user_id)
            await message.delete()
