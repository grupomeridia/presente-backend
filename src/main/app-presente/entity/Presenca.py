#Roberto
from entity.PresencaEnum import TipoPresenca
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

    def __init__(self, id:int, ativo:bool, aluno_ra:int, turma_id:int, projeto_id:int, chamada_id:int, professor_id:int, tipo_presenca:TipoPresenca, horario:datetime):
        self._id = id
        self._ativo = ativo
        self._aluno_ra = aluno_ra
        self._turma_id = turma_id
        self._projeto_id = projeto_id
        self._chamada_id = chamada_id
        self._professor_id = professor_id
        self._tipo_presenca = tipo_presenca
        self._horario = horario
