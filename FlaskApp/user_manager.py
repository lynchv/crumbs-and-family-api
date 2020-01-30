import os, yaml, re
from flask import abort
from flask_login import login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from FlaskApp import db
from FlaskApp.models.user import User


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


    def login_user(self, login_info):
        # Verify user is not already logged in
        if current_user.is_authenticated:
            print("User {} was already logged in".format(current_user.id))
            self.response['data'] = current_user.to_json()
        else:
            user = User.query.filter_by(email = login_info['email']).one_or_none()
            if not user or not check_password_hash(user.password, login_info['password']):
                abort(400, "Please check login details and try again.")
            login_user(user)
            self.response['data'] = user.to_json()


    def logout_user(self):
        if current_user.is_authenticated:
            print("Logging out user id {}".format(current_user.id))
            logout_user()
        else:
            m.response['message'] = "Trying to logout without being logged in."


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