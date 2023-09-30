from entity.TurnoEnum import Turno
from entity.ModalidadeEnum import Modalidade
from entity.CursoEnum import Curso
from models import db


class Turma(db.Model):
    __tablename__ = 'turmas'
    id_turma = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    semestre = db.Column(db.Integer, nullable=False)
    turno = db.Column(db.Enum(Turno))
    modalidade = db.Column(db.Enum(Modalidade))
    curso = db.Column(db.Enum(Curso))
    chamadas = db.relationship('Chamada', back_populates='turma')
    alunos = db.relationship('Aluno', secondary='turma_aluno')
    professores = db.relationship('Professor', secondary='turma_professor')

    def __init__(self, status:bool, nome:str, ano:int, semestre:int, turno:Turno, modalidade:Modalidade, curso:Curso):
        self.status = status
        self.nome = nome
        self.ano = ano
        self.semestre = semestre
        self.turno = turno
        self.modalidade = modalidade
        self.curso = curso
  


    
