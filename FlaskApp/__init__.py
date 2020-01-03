from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# Create  basic flask app with required config
app = Flask(__name__)
cors = CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create a flask-sqlalchemy hook
db = SQLAlchemy(app)

# Register the restplus API
from FlaskApp.routes import api
api.init_app(app, doc='/api')
