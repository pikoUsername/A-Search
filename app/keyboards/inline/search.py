from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


search_choice_btns = [
    [
        InlineKeyboardButton(text="Google", callback_data="config_search_google"),
    ]
]

search_choice_kb = InlineKeyboardMarkup(inline_keyboard=search_choice_btns)
