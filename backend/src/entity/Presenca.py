from entity.PresencaEnum import TipoPresenca
from models import db

from datetime import datetime

class Presenca(db.Model):
    __tablename__ = 'presencas'
    id_presenca = db.Column(db.Integer, primary_key=True)
    id_aluno = db.Column(db.Integer, db.ForeignKey('alunos.id_aluno'))
    id_chamada = db.Column(db.Integer, db.ForeignKey('chamadas.id_chamada'))
    status = db.Column(db.Boolean, nullable=False)
    horario = db.Column(db.DateTime)
    tipo_presenca = db.Column(db.Enum(TipoPresenca))
    cargo_manual = db.Column(db.String)
    id_manual = db.Column(db.Integer)
    aluno = db.relationship('Aluno', back_populates='presencas')
    chamada = db.relationship('Chamada', back_populates='presencas')

    def __init__(self, id_aluno:int, id_chamada:int, status:bool, tipo_presenca:TipoPresenca, cargo_manual:str, id_manual:int, horario:datetime):
        self.id_aluno = id_aluno
        self.id_chamada = id_chamada
        self.status = status
        self.tipo_presenca = tipo_presenca
        self.cargo_manual = cargo_manual
        self.id_manual = id_manual
        self.horario = horario
