from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from entity.Presenca import Presenca
from repository.MainRepository import MainRepository

class PresencaRepository(MainRepository.db.Model):

    def __init__():
        pass