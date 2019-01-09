from os import getenv
from os.path import abspath, dirname, join

basedir = abspath(dirname(__file__))


class Config:
    SECRET_KEY = getenv("SECRET_KEY") or "s3cRe7-kE4"
    SQLALCHEMY_DATABASE_URI = (
        getenv("DATABASE_URI") or f"sqlite:///{join(basedir, 'database.db')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite://"
