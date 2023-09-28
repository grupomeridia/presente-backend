from repository.MainRepository import MainRepository
import datetime

class Painel(MainRepository.db.Model):
    __tablename__ = 'painel'
    id_painel = MainRepository.db.Column(MainRepository.db.Integer, primary_key=True)
    id_configuracao = MainRepository.db.Column(MainRepository.db.ForeignKey('configuracoes.id_configuracao'))
    id_secretaria = MainRepository.db.Column(MainRepository.db.ForeignKey('secretaria.id_secretaria'))
    data = MainRepository.db.Column(MainRepository.db.DateTime, nullable=False)
    totalAtivos = MainRepository.db.Column(MainRepository.db.Integer, nullable=False)
    totalPresentes = MainRepository.db.Column(MainRepository.db.Integer, nullable=False)
    totalAusentes = MainRepository.db.Column(MainRepository.db.Integer, nullable=False)
    totalPresentesCurso = list
    totalAtivoCurso = list
    totalAusenteCurso = list
    configuracao = MainRepository.db.relationship('Configuracao', back_populates='painel')
    secretaria = MainRepository.db.relationship('Secretaria', back_populates='painel')

    def __init__(self, data:datetime, totalAtivos:int, totalPresentes:int, totalAusentes:int, totalPresentesCurso:list, totalAtivoCurso:list, totalAusenteCurso:list):
        self.data = data
        self.totalAtivos = totalAtivos
        self.totalPresentes = totalPresentes
        self.totalAusentes = totalAusentes
        self.totalPresentesCurso = totalPresentesCurso
        self.totalAtivoCurso = totalAtivoCurso
        self.totalAusenteCurso = totalAusenteCurso