from pathlib import Path
from typing import Union, Any
import os

from dotenv import load_dotenv

load_dotenv()


def get_env(key: str, default: Union[str, int] = None, type_: str = "str") -> Any:
    if type_ != "str":
        if type_ == "int":
            return os.getenv(key, default)
        elif type_ == "list":
            return [os.getenv(key, default)]
        elif type_ == "tuple":
            result: tuple = (os.getenv(key, default),)
            return result
        else:
            raise TypeError("Type Not Allowed")
    return str(os.getenv(key, default))


POSTGRES_NAME = get_env("DB_NAME", None)
POSTGRES_HOST = get_env("DB_HOST", None)
POSTGRES_PORT = get_env("DB_PORT", type_="int")
POSTGRES_USER = get_env("DB_USER", "user")
POSTGRES_PASS = get_env("DB_PASS", None)
POSTGRES_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_NAME}"

TOKEN = get_env("BOT_TOKEN", None)
ADMIN_IDS = get_env("ADMIN_IDS", None, "tuple")

REDIS_ON = get_env("REDIS_ON", None)

REDIS_HOST = get_env("REDIS_HOST", default="localhost")
REDIS_PORT = get_env("REDIS_PORT", default=6379)
REDIS_DB_FSM = get_env("REDIS_DB_FSM", default=0)

LOGS_BASE_PATH = str(Path(__name__).parent.parent / "logs")