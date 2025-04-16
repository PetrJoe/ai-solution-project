import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:password@localhost/dbcomparison'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/dbcomparison'
