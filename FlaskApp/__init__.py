from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Create  basic flask app with required config
app = Flask(__name__)
cors = CORS(app)
app.config['SECRET_KEY'] = '^sQjs^Q0hz51^FXuR6$rrI$VF2sd&qXb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create a flask-sqlalchemy db object
db = SQLAlchemy(app)

# Register the restplus API
from FlaskApp.routes import api
api.init_app(app, doc='/api')

# Create login manager
from FlaskApp.models.user import User
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))