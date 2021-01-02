from sqlalchemy import sql

from .base import TimedBaseModel, db


class Chat(TimedBaseModel):
    __tablename__ = "chats"

    query: sql.Select

    id = db.Column(db.Integer, index=True, primary_key=True)
    cid = db.Column(db.BigInteger)
    type = db.Column(db.String(20))
