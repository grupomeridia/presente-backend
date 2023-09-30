from models import db
from datetime import datetime

class Configuracao(db.Model):
    __tablename__ = 'configuracoes'
    id_configuracao = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, nullable=False)
    aluno_ausente = db.Column(db.Integer, nullable=False)
    inicio_aula = db.Column(db.DateTime, nullable=False)
    fim_aula = db.Column(db.DateTime, nullable=False)
    painel = db.relationship('Painel', back_populates='configuracao')

    def __init__(self, status:bool, aluno_ausente:int, inicio_aula:datetime, fim_aula:datetime):
        self.status = status
        self.aluno_ausente = aluno_ausente
        self.inicio_aula = inicio_aula
        self.fim_aula = fim_aula

