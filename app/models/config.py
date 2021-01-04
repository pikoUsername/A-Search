from sqlalchemy import sql

from .base import db, TimedBaseModel


class Config(TimedBaseModel):
    __tablename__ = "config"

    query: sql.Select

    id = db.Column(db.Integer, index=True, primary_key=True)
    on_user = db.ForeignKey('User', ondelete='CASCADE')
    search_language = db.Column(db.String(20), default=None)
    max_results = db.Column(db.Integer, default=10)
