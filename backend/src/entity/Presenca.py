from entity.PresencaEnum import TipoPresenca
from repository.MainRepository import MainRepository
import datetime

class Presenca(MainRepository.db.Model):
    __tablename__ = 'presencas'
    idPresenca = MainRepository.db.Column(MainRepository.db.Integer, primary_key=True)
    idAluno = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('alunos.idAluno'))
    idChamada = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('chamadas.idChamada'))
    status = MainRepository.db.Column(MainRepository.db.Boolean, nullable=False)
    horario = MainRepository.db.Column(MainRepository.db.DateTime)
    tipoPresenca = MainRepository.db.Column(MainRepository.db.Enum(TipoPresenca))
    aluno = MainRepository.db.relationship('Aluno', back_populates='presencas')
    chamada = MainRepository.db.relationship('Chamada', back_populates='presencas')

    def __init__(self, status:bool, tipoPresenca:TipoPresenca, horario:datetime):
        self.status = status
        self.tipoPresenca = tipoPresenca
        self.horario = horario
