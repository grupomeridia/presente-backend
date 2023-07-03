#Roberto
from entity.PresencaEnum import TipoPresenca
#from entity.Projeto import Projeto

from repository.MainRepository import MainRepository

import datetime

class Presenca(MainRepository.db.Model):
    
    id = MainRepository.db.Column(MainRepository.db.Integer, primary_key=True)
    ativo = MainRepository.db.Column(MainRepository.db.Boolean, nullable=False)
    aluno_ra = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('aluno.ra'))
    turma_id = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('turma.id'))
    projeto_id = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('projeto.id'))
    chamada_id = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('chamada.id'))
    professor_id = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('professor.id'))
    tipo_presenca = MainRepository.db.Column(MainRepository.db.Enum(TipoPresenca))
    horario = MainRepository.db.Column(MainRepository.db.DateTime(timezone=True))
    aluno = MainRepository.db.relationship('Aluno')
    turma = MainRepository.db.relationship('Turma')
    projeto = MainRepository.db.relationship('Projeto')
    chamada = MainRepository.db.relationship('Chamada')
    professor = MainRepository.db.relationship('Professor')

    def __init__(self, ativo:bool, aluno_ra:int, turma:int, projeto:int, chamada:int, professor:int, tipo_presenca:TipoPresenca, horario:datetime):
        self.ativo = ativo
        self.aluno_ra = aluno_ra
        self.turma_id = turma
        self.projeto_id = projeto
        self.chamada_id = chamada
        self.professor_id = professor
        self.tipo_presenca = tipo_presenca
        self.horario = horario
