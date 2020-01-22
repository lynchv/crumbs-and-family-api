from flask import request
from flask_login import login_user, logout_user
from flask_restplus import Namespace, Resource, fields
from FlaskApp.user_manager import UserMananager

api = Namespace('user', description='Namespace to interact with users.')

login_model = api.model('LoginModel', {
    'email': fields.String(required=True),
    'password': fields.String(required=True),
})

user_model = api.model('UserModel', {
    'first_name': fields.String(required=True),
    'last_name': fields.String(required=True),
    'email': fields.String(required=True),
    'password': fields.String(required=True),
})


@api.route('/login')
class LoginUser(Resource):
    @api.expect(login_model)
    def post(self):
        m = UserMananager()
        user = m.verify_login(request.json)
        login_user(user)
        return m.response


@api.route('/logout')
class LogoutUser(Resource):
    def get(self):
        m = UserMananager()
        logout_user()
        return m.response


@api.route('/')
class CreateUser(Resource):
    @api.expect(user_model)
    def post(self):
        m = UserMananager()
        m.create_user(request.json)
        return m.response

