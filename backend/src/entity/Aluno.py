from entity.Turma import Turma
from entity.CursoEnum import Curso
from entity.Presenca import Presenca

from repository.MainRepository import MainRepository


    
class Aluno(MainRepository.db.Model):
    id = MainRepository.db.Column(MainRepository.db.Integer, primary_key=True)
    ativo = MainRepository.db.Column(MainRepository.db.Boolean, nullable=False)
    nome = MainRepository.db.Column(MainRepository.db.String, nullable=False)
    ra = MainRepository.db.Column(MainRepository.db.Integer, nullable=False, unique=True)
    turma_id = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('turma.id'))
    turma = MainRepository.db.relationship('Turma')
    curso = MainRepository.db.Column(MainRepository.db.Enum(Curso))

    

    def __init__(self, ativo:bool,nome:str, RA:int, turmaId:int, curso:Curso):
        self.ativo = ativo
        self.nome = nome
        self.ra = RA
        self.turma_id = turmaId
        self.curso = curso
        



