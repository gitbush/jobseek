from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from jobseek.config import Config 

# instance of sqlalchemy 
db = SQLAlchemy()
# attach flask-wtf csrf token to app
csrf = CSRFProtect()
# login manager
login_manager = LoginManager()
# redirects to login if user tries to manually enter job_post via url
login_manager.login_view = 'employers.login'
login_manager.login_message_category = 'info'


def create_app(config_class=Config):
    # instance of flask 
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)


    from jobseek.users.routes import employers
    from jobseek.job_posts.routes import posts
    from jobseek.main.routes import main

    app.register_blueprint(employers)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    return app
