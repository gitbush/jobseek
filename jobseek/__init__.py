from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from jobseek.config import Config 

# instance of flask 
app = Flask(__name__)
app.config.from_object(Config)
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