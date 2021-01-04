from aiogram import types
from aiogram.types import ContentType
from loguru import logger

from ..loader import dp, bot
from ..keyboards.inline import start_kb
from ..models import dbc
from ..state import start


@dp.message_handler(commands=["start", "help"])
async def bot_start(message: types.Message):
    await start.MainMenuState.main_menu.set()
    return await message.answer("Этот Бот Создан для Поиска В Поисковых Системах.\n И этот Бот Имеет кастомизацию запросов типичную...\n",
                                reply_markup=start_kb)


@dp.message_handler(content_types=ContentType.TEXT)
async def bot_search(message: types.Message):
    if len(message.text) >= 1228:
        return await message.answer("Ваш Запрос Привысил Огранечение в 1227 букв. И он отклоняется")
    user = dbc.get_user_by_id(message.from_user.id)
    try:
        result = await dbc.search_query(user, message.text)
    except ValueError:
        result = None
    except TypeError as e:
        logger.error(e)
        raise e
        # return await message.reply("Сообщение Должно Быть больше 5 символов")

    if not result:
        return await message.reply("Ошибка, Нечего Не было Показано")
    return await message.answer(result)

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
    return await query.message.edit_text("Этот Бот Создан для Поиска В Поисковых Системах.\n И этот Бот НЕ РАБОТАЕТ...\n",
                                         reply_markup=start_kb)
