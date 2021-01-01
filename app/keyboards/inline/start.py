from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


start_btns = [
    [
        InlineKeyboardButton("Настройки", callback_data="start_menu_settings"),
        InlineKeyboardButton("Справка", callback_data="start_menu_help"),
        InlineKeyboardButton("Мета Информация", callback_data="start_menu_meta_info"),
    ]
]

start_kb = InlineKeyboardMarkup(inline_keyboard=start_btns)
