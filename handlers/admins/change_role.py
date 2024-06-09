from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from database import check_admin, role_update
from keyboards.admins.admins import admins_panel, role_change

router = Router()


@router.message(Command('role'))
async def change_user_role(message: Message):
    if check_admin(message.from_user.id)[0] == 'admin':
        try:

            text = message.text.split(' ')


            #Бляха не понимаю но почему то пишет что message.reply_to_message
            # None пытался натыкать в ботеПапе но не получилось


            if message.reply_to_message:


                if text[1] == 'admin' or text[1] == 'worker' or text[1] == 'support':
                    role_update(role=text[1], username=message.reply_to_message.from_user.username)

                    await message.delete()
                else:
                    await message.answer('Нету такой роли')
            else:

                if text[2] == 'admin' or text[2] == 'worker' or text[2] == 'support':
                    role_update(role=text[2], username=text[1][1:])
                    await message.delete()
                    await message.answer(f'{text[1]} назначен {text[2]}')

                else:
                    await message.answer('Нету такой роли')
        except:
            await message.answer('Неправильно написана команда')
