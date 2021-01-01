from sqlalchemy import sql

from .base import db, TimedBaseModel


class Config(TimedBaseModel):
    query: sql.Select

    id = db.Column(db.Integer, index=True, primary_key=True)
    on_user = db.ForeignKey('User', ondelete='DO_NOTHING')
    search_language = db.Column(db.String(20))
    find_human = db.Column(db.Boolean)
    find_any = db.Column(db.Boolean)
