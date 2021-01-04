from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from cse import Search

from . import config

bot = Bot(config.TOKEN, parse_mode="HTML")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
search = Search(config.GOOGLE_API_KEY, session=bot.session)


def setup():
    from . import filters
    from . import middlewares

    filters.setup(dp)
    middlewares.setup(dp)
