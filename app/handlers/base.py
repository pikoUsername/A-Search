from aiogram import types
from aiogram.dispatcher.filters import CommandStart, CommandHelp
from aiogram.types import ContentType

from ..loader import dp
from ..keyboards.inline import start_kb


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    return await message.answer("Этот Бот Создан для Поиска В Поисковых Системах.\n И этот Бот Имеет кастомизацию запросов тичичную...\n",
                                reply_markup=start_kb)


@dp.message_handler(content_types=ContentType.TEXT)
async def search(message: types.Message, user: User):
    if message.text >= 1228:
        return message.answer("Ваш Запрос Привысил Огранечение в 1227 букв. И он откланается")

