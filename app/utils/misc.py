from loguru import logger

from ..models.base import db
from ..config import POSTGRES_URI


async def on_startup(dp):
    bind = await db.set_bind(POSTGRES_URI)

    await db.gino.create_all(bind=bind)


async def on_shutdown(dp):
    bind = db.pop_bind()
    if bind:
        logger.info("Closing Postgres Connection")
        await db.gino.drop_all(bind=bind)
        await bind.close()
