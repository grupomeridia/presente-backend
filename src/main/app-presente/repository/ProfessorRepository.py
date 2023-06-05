from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from entity.Professor import Professor
from repository.MainRepository import MainRepository


class ProfessorRepository(MainRepository.db.Model):

    def __init__():
        pass