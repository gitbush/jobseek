import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager

# instance of flask 
app = Flask(__name__)
# evironment variables
app.config['SECRET_KEY'] = os.urandom(32)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# instance of sqlalchemy 
db = SQLAlchemy(app)
# attach flask-wtf csrf token to app
csrf = CSRFProtect()
csrf.init_app(app)
# login manager
login_manager = LoginManager(app)
# redirects to login if user tries to manually enter job_post via url
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'