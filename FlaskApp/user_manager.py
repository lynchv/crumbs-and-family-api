import os, yaml, re
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
            "message": "",
        }


    def create_user(self, user_info):
        user = User.query.filter_by(email = user_info['email']).one_or_none()
        
        if user:
            abort(400, "Email already in use.")
        self._verify_user_info(user_info)

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

        
    def _verify_user_info(self, user_info):
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

        if len(user_info['first_name']) < 1:
            abort(400, "First name can not be empty")
        if len(user_info['last_name']) < 1:
            abort(400, "Last name can not be empty")
        if not re.search(regex, user_info['email']):
            abort(400, "Please provide a valid email address")
        if len(user_info['password']) < 7:
            abort(400, "Please enter a password with at least 8 characters")