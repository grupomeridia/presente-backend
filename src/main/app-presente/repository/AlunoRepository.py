from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from entity.Aluno import Aluno
from repository.MainRepository import MainRepository

class AlunoRepository(MainRepository.db.Model):

    
    def __init__():
        pass

    def criarTabela(app:MainRepository.app, db:MainRepository.db):
        with app.app_context():
            db.create_all()
    