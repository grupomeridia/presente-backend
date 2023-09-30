TESTING = True
DEBUG = False
WTF_CSRF_ENABLED = False
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/app_presente'
SQLALCHEMY_TRACK_MODIFICATIONS = False
# password hash method
PROJECT_PASSWORD_HASH_METHOD = 'md5'

PROJECT_PASSWORD_HASH_METHOD = 'pbkdf2:sha1'
PROJECT_SITE_NAME = u'Flask Example'
PROJECT_SITE_URL = u'http://127.0.0.1:5000'
PROJECT_SIGNUP_TOKEN_MAX_AGE = 60 * 60 * 24 * 7  # in seconds
PROJECT_RECOVER_PASSWORD_TOKEN_MAX_AGE = 60 * 60 * 24 * 7  # in seconds