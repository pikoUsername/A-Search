from typing import Optional

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from ..models import dbc, User, Chat


class AclMiddleware(BaseMiddleware):
    async def setup_chat(self, data: dict, tg_user: types.User, tg_chat: Optional[types.Chat] = None):
        user_id = tg_user.id
        chat_id = tg_chat.id if tg_chat else tg_user.id

        user = await User.get(user_id)
        if not user:
            user = await dbc.add_new_user(tg_user)
        chat = await Chat.get(chat_id)
        if not chat:
            chat = await dbc.add_new_chat(tg_chat)

        data["user"] = user
        data["chat"] = chat

    async def on_pre_process_message(self, message: types.Message, data: dict):
        await self.setup_chat(data, message.from_user, message.chat)

    async def on_pre_process_callback_query(self, query: types.CallbackQuery, data: dict):
        await self.setup_chat(data, query.from_user, query.message.chat if query.message else None)