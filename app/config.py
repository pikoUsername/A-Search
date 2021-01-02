from pathlib import Path
from typing import Union, Any
import os
import secrets

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
        elif type_ == "boolean":
            return os.getenv(key, default)
        else:
            raise TypeError("Type Not Allowed")
    return str(os.getenv(key, default))


DOMAIN = get_env("DOMAIN", default="example.com")
SECRET_KEY = secrets.token_urlsafe(48)
WEBHOOK_BASE_PATH = get_env("WEBHOOK_BASE_PATH", default="/webhook")
WEBHOOK_PATH = f"{WEBHOOK_BASE_PATH}/{SECRET_KEY}"
WEBHOOK_URL = f"https://{DOMAIN}{WEBHOOK_PATH}"

POSTGRES_NAME = get_env("DB_NAME", None)
POSTGRES_HOST = get_env("DB_HOST", None)
POSTGRES_PORT = get_env("DB_PORT", type_="int")
POSTGRES_USER = get_env("DB_USER", "user")
POSTGRES_PASS = get_env("DB_PASS", None)
POSTGRES_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_NAME}"

TOKEN = get_env("BOT_TOKEN", None)
ADMIN_IDS = get_env("ADMIN_IDS", None, "tuple")

LOGS_BASE_PATH = str(Path(__name__).parent.parent / "logs")