import os, yaml
from flask import abort
from FlaskApp import db
from FlaskApp.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash


class UserMananager(object):
    def __init__(self):
        file_dir = os.path.dirname(__file__)
        with open(os.path.join(file_dir, "config.yaml")) as f:
            self.cfg = yaml.load(f, Loader=yaml.FullLoader)

        self.response = {
            "data": None,
            "error": "",
            "warning": "",
        }


    def create_user(self, user_info):
        user = User.query.filter_by(email = user_info['email']).one_or_none()
        if user:
            abort(400, "Email already in use.")

        password = generate_password_hash(user_info['password'], method='sha256')

        new_user = User(
            first_name = user_info['first_name'],
            last_name = user_info['last_name'],
            email = user_info['email'],
            password = password,
            is_admin = True if user_info['email'] in self.cfg['admin_emails'] else False
        )

        db.session.add(new_user)
        db.session.commit()

        self.response['data'] = True


    def verify_login(self, login_info):
        user = User.query.filter_by(email = login_info['email']).one_or_none()
        
        if not user or not check_password_hash(user.password, login_info['password']):
            abort(400, "Please check login details and try again.")
        self.response['data'] = user.to_json()
        
        return user

        
