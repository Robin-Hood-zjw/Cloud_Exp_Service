from db import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.string(80), unique=False, nullable=False)
    password = db.Column(db.string(80), nullable=False)