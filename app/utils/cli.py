import functools

import click
from loguru import logger
import aiohttp_autoreload

from .misc import on_startup, on_shutdown


@click.group()
def cli():
    from . import logging
    from .. import loader

    logging.setup()
    loader.setup()


def auto_reload_mixin(func):
    @click.option(
        "--autoreload", is_flag=True, default=False, help="Reload application on file changes"
    )
    @functools.wraps(func)
    def wrapper(autoreload: bool, *args, **kwargs):
        if autoreload and aiohttp_autoreload:
            logger.warning(
                "Application started in live-reload mode. Please disable it in production!"
            )
            aiohttp_autoreload.start()
        elif autoreload and not aiohttp_autoreload:
            click.echo("`aiohttp_autoreload` is not installed.", err=True)
        return func(*args, **kwargs)


@cli.command()
@auto_reload_mixin
def start_bot():
    from aiogram import executor
    from ..handlers import dp

    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
