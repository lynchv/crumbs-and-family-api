from flask_login import UserMixin
from FlaskApp import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100), default='', nullable=False)
    last_name = db.Column(db.String(100), default='', nullable=False)
    email = db.Column(db.String(100), default='', unique=True, nullable=False)
    password = db.Column(db.String(255), default='', nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def to_json(self):
        user_json = {}

        user_json['id'] = self.id
        user_json['first_name'] = self.first_name
        user_json['last_name'] = self.last_name
        user_json['is_admin'] = self.is_admin

        return user_json
