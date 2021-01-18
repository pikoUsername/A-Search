from aiogram import types
from aiogram.dispatcher.webhook import SendMessage, EditMessageText

from ..loader import dp, bot
from ..keyboards.inline import start_kb
from ..state import start


@dp.message_handler(commands=["start", "help"])
async def bot_start(message: types.Message):
    await start.MainMenuState.main_menu.set()
    return SendMessage(
        message.message_id,
        "Этот Бот Создан для Поиска В Поисковых Системах.\n И этот Бот Имеет кастомизацию запросов типичную...\n",
        reply_markup=start_kb
    )


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
    await start.MainMenuState.help_menu.set()


@dp.callback_query_handler(text="back_to_main_menu", state="*")
async def get_main_menu(query: types.CallbackQuery):
    await start.MainMenuState.main_menu.set()
    return EditMessageText(
        "Этот Бот Создан для Поиска В Поисковых Системах.\n И этот Бот НЕ РАБОТАЕТ...\n",
        query.message.chat.id,
        reply_markup=start_kb,
        message_id=query.message.message_id,
    )
