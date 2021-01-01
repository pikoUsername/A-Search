from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.dispatcher.storage import BaseStorage

from . import config

bot = Bot(config.TOKEN)

if config.REDIS_ON:
    storage = RedisStorage2(host=config.REDIS_HOST, port=config.REDIS_PORT, db=config.REDIS_DB_FSM)
else:
    storage = BaseStorage()
dp = Dispatcher(bot, storage=storage)


def setup():
    from . import filters
    from . import middlewares

    filters.setup(dp)
    middlewares.setup(dp)
