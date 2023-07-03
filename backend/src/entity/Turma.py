from repository.MainRepository import MainRepository

from entity.Chamada import Chamada
from entity.Presenca import Presenca

class Turma(MainRepository.db.Model):
    
    id = MainRepository.db.Column(MainRepository.db.Integer, primary_key=True)
    ativo = MainRepository.db.Column(MainRepository.db.Boolean, nullable=False)
    nome = MainRepository.db.Column(MainRepository.db.String(50), nullable=False)
    ano = MainRepository.db.Column(MainRepository.db.Integer, nullable=False)
    semestre = MainRepository.db.Column(MainRepository.db.String(1), nullable=False)

    def __init__(self, ativo, nome, ano, semestre):
        self.ativo = ativo
        self.nome = nome
        self.ano = ano
        self.semestre = semestre

  


    
