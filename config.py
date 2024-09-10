import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://postgres:Roma100@localhost/blog_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
