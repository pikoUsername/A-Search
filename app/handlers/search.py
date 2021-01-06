from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType, Message
from aiogram.dispatcher.handler import ctx_data
from cse import QuotaExceededError

from ..models import dbc, User
from ..loader import dp


@dp.message_handler(content_types=ContentType.TEXT, state="*")
async def bot_search(message: Message, state: FSMContext):
    if await state.get_state():
        return await message.delete()

    if len(message.text) >= 1228:
        return await message.answer("Ваш Запрос Привысил Огранечение в 1227 букв. И он отклоняется")

    data = ctx_data.get()
    user: User = data["user"]
    try:
        result = await dbc.search_query(user, message.text)
    except ValueError:
        return await message.reply("Ошибка, Нечего Не было Показано")
    except KeyError:
        return await message.answer("Результатов Не найдено((")
    except QuotaExceededError:
        return await message.answer("Бот Исчерпал лимит в 100 запросов в день")
    return await message.answer(result, disable_web_page_preview=True)