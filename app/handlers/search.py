from aiogram.types import ContentType, Message
from aiogram.dispatcher.handler import ctx_data

from ..models import dbc, User
from ..loader import dp


@dp.message_handler(content_types=ContentType.TEXT)
async def bot_search(message: Message):
    if len(message.text) >= 1228:
        return await message.answer("Ваш Запрос Привысил Огранечение в 1227 букв. И он отклоняется")

    data = ctx_data.get()
    user: User = data["user"]
    try:
        result = await dbc.search_query(user, message.text)
    except ValueError:
        result = None
    except KeyError:
        return await message.answer("Запрос Прывысил лимит google.")

    if not result:
        return await message.reply("Ошибка, Нечего Не было Показано")
    return await message.answer(result, disable_web_page_preview=True)