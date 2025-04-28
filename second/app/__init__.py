from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object(Config)

# PostgreSQL connection
db = SQLAlchemy(app)

# MongoDB connection
mongo_client = MongoClient(app.config['MONGO_URI'])
mongo_db = mongo_client.get_database()

from app.scripts import routes
