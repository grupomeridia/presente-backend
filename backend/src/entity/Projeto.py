from repository.MainRepository import MainRepository

from entity.Chamada import Chamada
from entity.Configuracao import Configuracao

class Projeto(MainRepository.db.Model):
    id = MainRepository.db.Column(MainRepository.db.Integer, primary_key=True)
    ativo = MainRepository.db.Column(MainRepository.db.Boolean, nullable=False)
    nome = MainRepository.db.Column(MainRepository.db.String, nullable=False)
    configuracao = MainRepository.db.relationship('Configuracao', backref='projeto')

    def __init__(self, ativo:bool, nome:str):
        self.ativo = ativo
        self.nome = nome
