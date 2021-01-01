from typing import Optional

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from ..models import dbc, User, Chat


class AclMiddleware(BaseMiddleware):
    async def setup_chat(self, data: dict, user: types.User, chat: Optional[types.Chat] = None):
        user_id = user.id
        chat_id = chat.id if chat else user.id

        user = await dbc.get_chat_by_id(user_id)
        if user is None:
            user = await dbc.add_new_user(user)
        chat = await dbc.get_chat_by_id(chat_id)
        if chat is None:
            chat = await dbc.add_new_chat(chat)

        data["user"] = user
        data["chat"] = chat

    async def on_pre_process_message(self, message: types.Message, data: dict):
        await self.setup_chat(data, message.from_user, message.chat)

    async def on_pre_process_callback_query(self, query: types.CallbackQuery, data: dict):
        await self.setup_chat(data, query.from_user, query.message.chat if query.message else None)