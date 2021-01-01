import datetime
from typing import List

import sqlalchemy as sa

from gino import Gino

db = Gino()


class BaseModel(db.Model):
    __abstaract__ = True

    @classmethod
    def __tablename__(cls):
        if getattr(cls, "__tablename__", None) is not None:
            return cls.__tablename__

        name = cls.__name__.lower()
        if getattr(cls, "__abstract__", None) is None:
            return name
        return None
    __tablename__ = __tablename__()

    def __str__(self):
        model = self.__class__.__name__
        table: sa.Table = sa.inspect(self.__class__)
        primary_key_columns: List[sa.Column] = table.primary_key.columns
        values = {
            column.name: getattr(self, self._column_name_map[column.name])
            for column in primary_key_columns
        }
        values_str = " ".join(f"{name}={value!r}" for name, value in values.items())
        return f"<{model} {values_str}>"


class TimedBaseModel(BaseModel):
    __abstaract__ = True

    created_at = db.Column(db.DateTime(True), server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime(True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        server_default=db.func.now(),
    )