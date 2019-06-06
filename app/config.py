import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "postgresql://romeo:incorrect@localhost:5432/hexdb"
    SECRET_KEY = '@#$%^$^&ghdsfjkdlvd$%^&%&*(^'
