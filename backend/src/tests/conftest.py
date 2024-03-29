import pytest
from application import create_app
from models import db

@pytest.fixture()
def app():
    app = create_app('settings_test.py')
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
