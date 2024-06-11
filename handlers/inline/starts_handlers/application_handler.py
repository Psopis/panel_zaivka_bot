from aiogram import F
import datetime
from aiogram import Router
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from database.db_working import AdminWorking, ApplicationWorking
from keyboards.inline.application_in import application_accept
from keyboards.inline.chats import chats_for_subs

router = Router()
router.message.filter(
    F.chat.type == "private"
)


class Application_states(StatesGroup):
    url_lolz = State()
    experience = State()
    free_time = State()


@router.callback_query(F.data.contains('application_post'))
async def application_set(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.answer(text='Предоставтье ссылку')
    await state.set_state(Application_states.url_lolz)


@router.message(Application_states.url_lolz)
async def application_set(message: Message, state: FSMContext):
    await state.update_data(url=message.text)
    await message.answer(text='Какой у вас стаж работы?')
    await state.set_state(Application_states.experience)


@router.message(Application_states.experience)
async def application_set(message: Message, state: FSMContext):
    await state.update_data(exp=message.text)
    await message.answer(text='Сколько времени вы готовы уделаять?')
    await state.set_state(Application_states.free_time)


@router.message(Application_states.free_time)
async def application_set(message: Message, state: FSMContext):
    await state.update_data(free_time=message.text)
    data = await state.get_data()

    user_info = f"""\n
    ----НОВАЯ ЗАЯВКА----
    \n
    User :   {message.from_user.username}
    Date :   {datetime.date.today()}
    URL :   {data['url']}
    Expirience :   {data['exp']}
    Free Time :   {data['free_time']}
    """
    admins = await AdminWorking.get_all_admins_and_suppots()
    await ApplicationWorking.add_application(user_id=message.from_user.id,
                                             username=message.from_user.username,
                                             date=datetime.date.today(),
                                             url=data['url'],
                                             exp=data['exp'],
                                             free_time=data['free_time']
                                             )
    for i in admins:
        await message.bot.send_message(text=user_info, chat_id=i.userid,
                                       reply_markup=application_accept(message.from_user.id))

    await state.clear()


@router.callback_query(F.data.contains('application_accepted'))
async def application_post_acc(call: CallbackQuery):

    await call.answer()
    user_id = call.data.split('.')[1]
    print(user_id)
    await call.message.edit_reply_markup(
        reply_markup=InlineKeyboardBuilder().add(InlineKeyboardButton(text="✅", callback_data='no good')).as_markup())

    await call.bot.send_message(text='✅ Ваша заявка была одобрена администрацией.', chat_id=user_id)
    await ApplicationWorking.accept_app(user_id)
    await call.bot.send_message(text='Подпишитесь на эти каналы ', reply_markup=chats_for_subs().as_markup(),
                                chat_id=user_id)


@router.callback_query(F.data.contains('application_denial'))
async def application_post_deni(call: CallbackQuery):
    await call.answer()
    user_id = call.data.split('.')[1]
    await call.message.edit_reply_markup(
        reply_markup=InlineKeyboardBuilder().add(InlineKeyboardButton(text="❌", callback_data='good')).as_markup())

    await call.bot.send_message(text='❌ Ваша заявка не одобрена администрацией.', chat_id=user_id)
