from aiogram import types

from ..loader import dp
from ..keyboards.inline import config, search, start_kb
from ..state import start


@dp.callback_query_handler(text="start_menu_settings", state=start.MainMenuState.main_menu)
async def show_settings_menu(query: types.CallbackQuery):
    await start.MainMenuState.config_menu.set()
    return await query.message.edit_text("Настройки:", reply_markup=config.config_kb)


@dp.callback_query_handler(text="where_search", state=start.MainMenuState.config_menu)
async def choice_search_system(query: types.CallbackQuery):
    return await query.message.edit_text("Выбирите:", reply_markup=search.search_choice_kb)


@dp.callback_query_handler(text="config_search_google", state=start.MainMenuState.config_menu)
async def change_search_system(query: types.CallbackQuery):
     return await query.message.edit_text("Настройки: ", reply_markup=config.config_kb)


@dp.callback_query_handler(text="config_back", state=start.MainMenuState.config_menu)
async def get_main_menu(query: types.CallbackQuery):
    await start.MainMenuState.main_menu.set()
    return await query.message.edit_text("Этот Бот Создан для Поиска В Поисковых Системах.\n И этот Бот Имеет кастомизацию запросов типичную...\n",
                                         reply_markup=start_kb)
