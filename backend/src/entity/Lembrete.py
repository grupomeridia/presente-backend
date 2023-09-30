from entity.CargoEnum import Cargo
from models import db
import datetime

class Lembrete(db.Model):
    __tablename__ = 'lembretes'
    id_lembrete = db.Column(db.Integer, primary_key=True)
    id_secretaria = db.Column(db.Integer, db.ForeignKey('secretaria.id_secretaria'))
    destinatario_cargo = db.Column(db.Enum(Cargo))
    destinatario_id = db.Column(db.Integer, nullable=False)
    titulo = db.Column(db.String(50), nullable=False)
    mensagem = db.Column(db.String(100), nullable=False)
    criacao = db.Column(db.DateTime, nullable=False)
    visualizacao = db.Column(db.DateTime)
    secretaria = db.relationship('Secretaria', back_populates='lembrete')

    def __init__(self, id_secretaria:int, destinatario_cargo:Cargo, destinatario_id:int, titulo:str, mensagem:str, criacao:datetime, visualizacao:datetime):
        self.id_secretaria = id_secretaria
        self.destinatario_cargo = destinatario_cargo
        self.destinatario_id = destinatario_id
        self.titulo = titulo
        self.mensagem = mensagem
        self.criacao = criacao
        self.visualizacao = visualizacao