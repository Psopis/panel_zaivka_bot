from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from database.db_working import UserWorking, AdminWorking

router = Router()
router.message.filter(
    F.chat.type == "private"
)


@router.message(Command('role'))
async def change_user_role(message: Message):
    if await AdminWorking.check_admin(message.from_user.id) == 'admin':

        text = message.text.split(' ')
        if message.reply_to_message:
            if text[1] == 'admin' or text[1] == 'worker' or text[1] == 'support' or text[1] == 'member':
                await UserWorking.role_update(username=message.reply_to_message.from_user.username, role=text[1])

                await message.delete()
            else:
                await message.answer('Нету такой роли')
                await message.delete()

        else:

            if text[2] == 'admin' or text[2] == 'worker' or text[2] == 'support' or text[2] == 'member':
                await UserWorking.role_update(username=text[1][1:], role=text[2])

                await message.delete()
                await message.answer(f'{text[1]} назначен {text[2]}')

            else:
                await message.answer('Нету такой роли')
                await message.delete()
        # try:
        #
        #
        #
        #     # Бляха не понимаю но почему то пишет что message.reply_to_message
        #     # None пытался натыкать в ботеПапе но не получилось
        #
        # except:
        #     await message.answer('Неправильно написана команда')
