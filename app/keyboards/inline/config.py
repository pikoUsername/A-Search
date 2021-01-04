from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


config_btns = [
    [
        InlineKeyboardButton(text="Где Искать", callback_data="where_search"),
        InlineKeyboardButton(text="Выбрать Регион", callback_data="choice_region"),
    ],
    [
        InlineKeyboardButton(text="<< Назад", callback_data="back_to_main_menu"),
    ]
]

config_kb = InlineKeyboardMarkup(inline_keyboard=config_btns)
