import sqlalchemy as sa

from .base import db, TimedBaseModel


class User(TimedBaseModel):
    query: sa.sql.Select

    id = db.Column(db.Integer, index=True, primary_key=True)
    uid = db.Column(db.BigInteger)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    search_language_type = db.Column(db.String(20))
    is_admin = db.Column(db.Boolean, default=sa.sql.expression.false())
    config = db.ForeignKey('Config', ondelete="CASCADE")
