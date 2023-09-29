from repository.MainRepository import MainRepository
import datetime

class Configuracao(MainRepository.db.Model):
    __tablename__ = 'configuracoes'
    id_configuracao = MainRepository.db.Column(MainRepository.db.Integer, primary_key=True)
    status = MainRepository.db.Column(MainRepository.db.Boolean, nullable=False)
    aluno_ausente = MainRepository.db.Column(MainRepository.db.Integer, nullable=False)
    inicio_aula = MainRepository.db.Column(MainRepository.db.DateTime, nullable=False)
    final_aula = MainRepository.db.Column(MainRepository.db.DateTime, nullable=False)
    painel = MainRepository.db.relationship('Painel', back_populates='configuracao')

    def __init__(self, status:bool, aluno_ausente:int, inicio_aula:datetime, final_aula:datetime):
        self.status = status
        self.aluno_ausente = aluno_ausente
        self.inicio_aula = inicio_aula
        self.final_aula = final_aula

