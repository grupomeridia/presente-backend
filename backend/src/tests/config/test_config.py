import settings

def teste_data_base_login(client):
    assert settings.DATABASE_LOGIN == "postgres"

def test_data_base_p(client):
    assert settings.DATABASE_PASS == "postgres"

def test_debug_is_false(client):
    assert settings.DEBUG == False

def test_testing_is_false(client):
    assert settings.TESTING == False

def test_secret_key_exists(client):
    assert settings.SECRET_KEY == "29904e38dc64706d8a61ad4525a7efd91c2f7022e4ab48ede425a6270687dd08"

def wtf_scrf_not_enabled(client):
    assert settings.WTF_CSRF_ENABLED == False

def MAIL_SENDER(client):
    assert settings.MAIL_DEFAULT_SENDER == 'noreply@yourmail.com'

def sqlachemy_database_exists(client):
    assert len(settings.SQLALCHEMY_DATABASE_URI) > 1