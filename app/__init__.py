from flask import Flask
from flask_restful import Api
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)