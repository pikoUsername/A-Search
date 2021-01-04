from typing import List, Dict

from aiogram import types
from cse import SearchResult, SearchError, Language
from loguru import logger

from .user import User
from .chat import Chat
from .. import config
from ..loader import search
from ..utils.lang import get_user_lang


class DBCommands:
    @staticmethod
    async def get_user_by_id(tg_id: int):
        user = await User.query.where(User.user_id == tg_id).gino.first()
        return user

    @staticmethod
    async def get_chat_by_id(chat_id: int):
        chat = await Chat.query.where(Chat.cid == chat_id).gino.first()
        return chat

    async def add_new_user(self, user: types.User):
        old_user = await self.get_user_by_id(user.id)
        if old_user:
            return old_user

        new_user = User()
        new_user.uid = user.id
        new_user.last_name = user.last_name
        new_user.first_name = user.first_name
        if config.ADMIN_IDS:
            new_user.is_admin = True

        await new_user.create()

    async def add_new_chat(self, chat: types.Chat):
        old_chat = await self.get_chat_by_id(chat.id)
        if old_chat:
            return old_chat

        new_chat = Chat()
        new_chat.cid = chat.id
        new_chat.type = chat.type

        await new_chat.create()

    async def search_query(self, user: User, text: str, max_results: int=10) -> str:
        user_lang = await get_user_lang(user)
        try:
            results = await search.search(
                query=text,
                max_results=max_results,
                language=user_lang
            )
        except SearchError as e:
            logger.error(str(e))
            raise e

        return "\n".join([f"{i.title} |\n{i.link}" for i in results])
