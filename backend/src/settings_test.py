import os

DATABASE_LOGIN = os.environ.get('DATABASE_LOGIN')
DATABASE_PASS = os.environ.get('DATABASE_SENHA')

TESTING = True
DEBUG = False
WTF_CSRF_ENABLED = False
SQLALCHEMY_DATABASE_URI = f'postgresql://{DATABASE_LOGIN}:{DATABASE_PASS}@localhost/app_presente'
SQLALCHEMY_TRACK_MODIFICATIONS = False



