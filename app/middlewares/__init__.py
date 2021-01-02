from aiogram import Dispatcher
from loguru import logger

from .acl import AclMiddleware
from .throtling import ThrottlingMiddleware


def setup(dp: Dispatcher):
    logger.info("Configure Middlewares...")

    dp.middleware.setup(AclMiddleware())
    dp.middleware.setup(ThrottlingMiddleware())
