from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


meta_btns = [
    [
        InlineKeyboardButton(text="Github", url="https://github.com/pikoUsername/A-Search"),
        InlineKeyboardButton(text="Описание", callback_data="description"),
    ],
    [
        InlineKeyboardButton(text="<< Назад", callback_data="back_to_main_menu"),
    ]
]

meta_kb = InlineKeyboardMarkup(inline_keyboard=meta_btns)
