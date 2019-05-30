import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "MUST PROVIDE DATABASE URL"
    SECRET_KEY = '@#$%^$^&ghdsfjkdlvd$%^&%&*(^'