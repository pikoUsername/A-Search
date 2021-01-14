from typing import List

from aiogram import types
from aiogram.dispatcher.webhook import EditMessageText

from ..loader import dp, bot
from ..state.start import MainMenuState
from ..keyboards.inline.meta import meta_kb


@dp.callback_query_handler(text="start_menu_meta_info", state=MainMenuState.main_menu)
async def get_meta_info(query: types.CallbackQuery):
    await query.message.edit_text("Мета Информация: ", reply_markup=meta_kb)
    await MainMenuState.meta_menu.set()


@dp.callback_query_handler(text="description", state=MainMenuState.meta_menu)
async def get_description(query: types.CallbackQuery):
    text: List[str] = [
        "Описание Бота:\n",
        "Этот Бот Создан Что бы Гуглить, Например",
        "Написав 'google it', Вы Получите результат как будто забив в строку поисковие 'google it'",
        "И конечено Запросы Можно Отчасти Кастомизировать",
    ]
    kb = types.InlineKeyboardMarkup(inline_keyboard=[
        [
            types.InlineKeyboardButton("<< Назад", callback_data="back_to_main_menu"),
        ],
    ])
    return EditMessageText("\n".join(text), reply_markup=kb)
