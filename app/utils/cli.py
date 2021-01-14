import functools

import click
from loguru import logger
import aiohttp_autoreload

from .misc import on_startup, on_shutdown
from ..config import WEBHOOK_URL


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

    return wrapper



@cli.command(name="polling")
@click.option("--skip-updates", is_flag=True, default=False, help="Skip pending updates")
@auto_reload_mixin
def polling(skip_updates: bool):
    """
    Start application in polling mode
    """
    from aiogram import executor
    from ..handlers import dp

    executor.start_polling(
        dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=skip_updates
    )


@cli.command()
@auto_reload_mixin
def webhook():
    from aiogram import executor
    from app.handlers import dp

    executor.start_webhook(
        dp,
        webhook_path=WEBHOOK_URL,
        on_startup=on_startup,
        on_shutdown=on_shutdown
    )
