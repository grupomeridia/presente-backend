import os

# -*- coding: utf-8 -*-
DATABASE_LOGIN = os.environ.get('DATABASE_LOGIN')
DATABASE_PASS = os.environ.get('DATABASE_SENHA')
# flask core settings
DEBUG = False
TESTING = False
SECRET_KEY = "29904e38dc64706d8a61ad4525a7efd91c2f7022e4ab48ede425a6270687dd08"
PERMANENT_SESSION_LIFETIME = 60 * 60 * 24 * 30

# flask wtf settings
WTF_CSRF_ENABLED = True

# flask mail settings
MAIL_DEFAULT_SENDER = 'noreply@yourmail.com'
SQLALCHEMY_DATABASE_URI = f'postgresql://{DATABASE_LOGIN}:{DATABASE_PASS}@localhost/app_presente'