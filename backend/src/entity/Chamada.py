import datetime
from models import db

class Chamada(db.Model):
    __tablename__ = 'chamadas'
    id_chamada = db.Column(db.Integer, primary_key=True)
    id_materia = db.Column(db.Integer, db.ForeignKey('materias.id_materia'))
    id_turma = db.Column(db.Integer, db.ForeignKey('turmas.id_turma'))
    id_professor = db.Column(db.Integer, db.ForeignKey('professores.id_professor'))
    status = db.Column(db.Boolean, nullable=False)
    abertura = db.Column(db.DateTime, nullable=False)
    encerramento = db.Column(db.DateTime)
    materia = db.relationship('Materia', back_populates='chamadas')
    turma = db.relationship('Turma', back_populates='chamadas')
    professor = db.relationship('Professor', back_populates='chamadas')
    presencas = db.relationship('Presenca', back_populates='chamada')
    
    def __init__(self, id_materia:int, id_turma:int, id_professor:int ,status:bool, abertura:datetime, encerramento:datetime):
        self.id_materia = id_materia
        self.id_turma = id_turma
        self.id_professor = id_professor
        self.status = status
        self.abertura = abertura
        self.encerramento = encerramento


