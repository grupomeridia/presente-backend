import os
from dotenv import load_dotenv

load_dotenv()

# -*- coding: utf-8 -*-
DATABASE_LOGIN = os.environ.get('DATABASE_LOGIN')
DATABASE_PASS = os.environ.get('DATABASE_SENHA')
# flask core settings
DEBUG = False
TESTING = False
SECRET_KEY = os.environ.get('SECRET_KEY')
PERMANENT_SESSION_LIFETIME = 60 * 60 * 24 * 30

# flask wtf settings
WTF_CSRF_ENABLED = os.environ.get('WTF_CSRF_ENABLED')

# flask mail settings
MAIL_DEFAULT_SENDER =os.environ.get('MAIL_DEFAULT_SENDER')
SQLALCHEMY_DATABASE_URI = f'postgresql://{DATABASE_LOGIN}:{DATABASE_PASS}@localhost/app_presente'