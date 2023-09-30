import os
import tempfile

import pytest

from flask import Flask
from repository.MainRepository import MainRepository

@pytest.fixture
def client():
    db_fd, MainRepository.app.config['DATABASE'] = tempfile.mkstemp()
    MainRepository.app.config['TESTING'] = True

    with MainRepository.app.test_client() as client:
        with MainRepository.app.app_context():
            MainRepository.app.init_db()
        yield client

    os.close(db_fd)