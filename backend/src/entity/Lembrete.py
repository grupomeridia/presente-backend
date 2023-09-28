from entity.CargoEnum import Cargo
from repository.MainRepository import MainRepository
import datetime

class Lembrete(MainRepository.db.Model):
    __tablename__ = 'lembretes'
    idLembrete = MainRepository.db.Column(MainRepository.db.Integer, primary_key=True)
    idSecretaria = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('secretaria.idSecretaria'))
    destinatarioCargo = MainRepository.db.Column(MainRepository.db.Enum(Cargo))
    destinatarioId = MainRepository.db.Column(MainRepository.db.Integer, nullable=False)
    titulo = MainRepository.db.Column(MainRepository.db.String(50), nullable=False)
    mensagem = MainRepository.db.Column(MainRepository.db.String(100), nullable=False)
    criacao = MainRepository.db.Column(MainRepository.db.DateTime, nullable=False)
    visualizacao = MainRepository.db.Column(MainRepository.db.DateTime)
    secretaria = MainRepository.db.relationship('Secretaria', back_populates='lembrete')

    def __init__(self, destinatarioCargo:Cargo, titulo:str, mensagem:str, criacao:datetime, visualizacao:datetime):
        self.destinatarioCargo = destinatarioCargo
        self.titulo = titulo
        self.mensagem = mensagem
        self.criacao = criacao
        self.visualizacao = visualizacao