from aiogram import types
from aiogram.dispatcher.webhook import EditMessageText

from ..loader import dp
from ..keyboards.inline import config, search
from ..state import start


@dp.callback_query_handler(text="start_menu_settings", state=start.MainMenuState.main_menu)
async def show_settings_menu(query: types.CallbackQuery):
    await start.MainMenuState.config_menu.set()
    return EditMessageText(
        "Настройки:",
        query.message.chat.id,
        message_id=query.message.message_id,
        reply_markup=config.config_kb,
    )


@dp.callback_query_handler(text="where_search", state=start.MainMenuState.config_menu)
async def choice_search_system(query: types.CallbackQuery):
    return EditMessageText(
        "Выбирите: ",
        query.message.chat.id,
        message_id=query.message.message_id,
        reply_markup=search.search_choice_kb,
    )


@dp.callback_query_handler(text_contains="config_search_google", state=start.MainMenuState.config_menu)
async def change_search_system(query: types.CallbackQuery):
    return EditMessageText(
        "Настройки: ",
        query.message.chat.id,
        message_id=query.message.message_id,
        reply_markup=config.config_kb,
    )
