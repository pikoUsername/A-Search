from aiogram import types
from aiogram.types import ContentType

from ..loader import dp, bot
from ..keyboards.inline import start_kb
from ..models import User
from ..state import start
from ..utils.search import search


@dp.message_handler(commands=["start", "help"])
async def bot_start(message: types.Message):
    await start.MainMenuState.main_menu.set()
    return await message.answer("Этот Бот Создан для Поиска В Поисковых Системах.\n И этот Бот Имеет кастомизацию запросов типичную...\n",
                                reply_markup=start_kb)


@dp.message_handler(content_types=ContentType.TEXT)
async def search(message: types.Message, user: User):
    if len(message.text) >= 1228:
        return message.answer("Ваш Запрос Привысил Огранечение в 1227 букв. И он отклоняется")
    pass  # here search query


@dp.callback_query_handler(text="start_menu_help", state=start.MainMenuState.main_menu)
async def get_help_menu(query: types.CallbackQuery):
    """
    Get To User Help Menu with all commands in inline keyboard

    :param query:
    :return:
    """


    commands = await bot.get_my_commands()
    commands_btns = []
    for command in commands:
        commands_btns.append([types.InlineKeyboardButton(text=command.command, callback_data=command.command)])
    commands_btns.append([types.InlineKeyboardButton(text="<< Назад", callback_data="back_to_main_menu")])
    commands_kb = types.InlineKeyboardMarkup(inline_keyboard=commands_btns)

    if commands_btns is None:
        return await query.message.edit_text("Здесь Нету Никаких Комманд", reply_markup=commands_kb)

    await query.message.edit_text("Справка По Коммандам\n", reply_markup=commands_kb)
    return await start.MainMenuState.help_menu.set()


@dp.callback_query_handler(text="back_to_main_menu", state="*")
async def get_main_menu(query: types.CallbackQuery):
    await start.MainMenuState.main_menu.set()
    return await query.message.edit_text("Этот Бот Создан для Поиска В Поисковых Системах.\n И этот Бот Имеет кастомизацию типичную...\n",
                                         reply_markup=start_kb)
