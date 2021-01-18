from .base import TimedBaseModel, db


class Chat(TimedBaseModel):
    __tablename__ = "chats"

    id = db.Column(db.Integer, index=True, primary_key=True, unique=True)
    cid = db.Column(db.BigInteger)
    type = db.Column(db.String(20))
