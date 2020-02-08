import os

class Config:
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')

    # untrack any changes to objects. Stop long message in terminal when running app
    SQLALCHEMY_TRACK_MODIFICATIONS = False
