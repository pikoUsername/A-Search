from cse import Language

from ..models import User


async def get_user_lang(user: User):
    try:
        return getattr(Language, str(user.config.search_language))
    except AttributeError as exc:
        return None