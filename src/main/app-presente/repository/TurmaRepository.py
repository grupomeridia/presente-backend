from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from entity.Turma import Turma
from repository.MainRepository import MainRepository

class TurmaRepository(MainRepository.db.Model):

    def __init__():
        pass