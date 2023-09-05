from repository.MainRepository import MainRepository
import datetime

class Painel(MainRepository.db.Model):
    __tablename__ = 'painel'
    idPainel = MainRepository.db.Column(MainRepository.db.Integer, primary_key=True)
    idConfiguracao = MainRepository.db.Column(MainRepository.db.ForeignKey('configuracoes.idConfiguracao'))
    idSecretaria = MainRepository.db.Column(MainRepository.db.ForegnKey('secretaria.idSecretaria'))
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