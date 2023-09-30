from models import db
import datetime

class Painel(db.Model):
    __tablename__ = 'painel'
    id_painel = db.Column(db.Integer, primary_key=True)
    id_configuracao = db.Column(db.ForeignKey('configuracoes.id_configuracao'))
    id_secretaria = db.Column(db.ForeignKey('secretaria.id_secretaria'))
    data_criado = db.Column(db.DateTime, nullable=False)
    total_ativos = db.Column(db.Integer, nullable=False)
    total_presentes = db.Column(db.Integer, nullable=False)
    total_ausentes = db.Column(db.Integer, nullable=False)
    total_presentes_curso = list
    total_ativo_curso = list
    total_ausente_curso = list
    configuracao = db.relationship('Configuracao', back_populates='painel')
    secretaria = db.relationship('Secretaria', back_populates='painel')

    def __init__(self, id_configuracao:int, id_secretaria:int, data_criado:datetime, total_ativos:int, total_presentes:int, total_ausentes:int, total_presentes_curso:list, total_ativo_curso:list, total_ausente_curso:list):
        self.id_configuracao = id_configuracao
        self.id_secretaria = id_secretaria
        self.data_criado = data_criado
        self.total_ativos = total_ativos
        self.total_presentes = total_presentes
        self.total_ausentes = total_ausentes
        self.total_presentes_curso = total_presentes_curso
        self.total_ativo_curso = total_ativo_curso
        self.total_ausente_curso = total_ausente_curso