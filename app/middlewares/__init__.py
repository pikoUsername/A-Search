from aiogram import Dispatcher
from loguru import logger

from .acl import AclMiddleware


def setup(dp: Dispatcher):
    logger.info("Configure Middlewares...")

    dp.middleware.setup(AclMiddleware)
