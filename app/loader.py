from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from . import config

bot = Bot(config.TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


def setup():
    from . import filters
    from . import middlewares

    filters.setup(dp)
    middlewares.setup(dp)
