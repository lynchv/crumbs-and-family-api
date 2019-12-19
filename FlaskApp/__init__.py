from flask import Flask
from FlaskApp.routes import api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

api.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
db = SQLAlchemy(app)

