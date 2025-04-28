import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/test'
    
    # Add a separate PostgreSQL connection string for psycopg2
    POSTGRESQL_DSN = os.environ.get('POSTGRESQL_DSN') or 'dbname=postgres user=postgres password=postgres host=localhost'
