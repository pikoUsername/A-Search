from aiogram import types
from aiogram.dispatcher.filters import ChatTypeFilter


@dp.message_handler(ChatTypeFilter('private'), commands="delete_")
async def delete(message: types.Message):
    pass
