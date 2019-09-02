import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

# load from .env file
load_dotenv(os.path.join(basedir,'.env'))

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///'+os.path.join(basedir,'app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    POSTS_PER_PAGE = 5
    LANGUAGES = ['en','zh']

    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # ADMINS = ['kanghui06@gmail.com']


    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'localhost'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 8025)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['rocksnow1942@gmail.com']

# to run a fake server: python -m smtpd -n -c DebuggingServer localhost:8025
