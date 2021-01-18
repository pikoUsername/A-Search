from .base import db, TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = "users5"

    id = db.Column(db.Integer, index=True, primary_key=True)
    user_id = db.Column(db.BigInteger)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    search_language_type = db.Column(db.String(20))
    is_admin = db.Column(db.Boolean, default=db.fund.false())
    config_id = db.Column(db.Integer, db.ForeignKey('config.id'))
