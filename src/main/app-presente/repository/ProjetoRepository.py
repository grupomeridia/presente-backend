from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from entity.Projeto import Projeto
from repository.MainRepository import MainRepository

class ProjetoRepository(MainRepository.db.Model):

    def __init__():
        pass