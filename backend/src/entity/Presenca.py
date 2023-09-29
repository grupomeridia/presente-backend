from entity.PresencaEnum import TipoPresenca
from repository.MainRepository import MainRepository
import datetime

class Presenca(MainRepository.db.Model):
    __tablename__ = 'presencas'
    id_presenca = MainRepository.db.Column(MainRepository.db.Integer, primary_key=True)
    id_aluno = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('alunos.id_aluno'))
    id_chamada = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('chamadas.id_chamada'))
    status = MainRepository.db.Column(MainRepository.db.Boolean, nullable=False)
    horario = MainRepository.db.Column(MainRepository.db.DateTime)
    tipo_presenca = MainRepository.db.Column(MainRepository.db.Enum(TipoPresenca))
    aluno = MainRepository.db.relationship('Aluno', back_populates='presencas')
    chamada = MainRepository.db.relationship('Chamada', back_populates='presencas')

    def __init__(self, id_aluno:int, id_chamada:int, status:bool, tipoPresenca:TipoPresenca, horario:datetime):
        self.id_aluno = id_aluno
        self.id_chamada = id_chamada
        self.status = status
        self.tipoPresenca = tipoPresenca
        self.horario = horario
