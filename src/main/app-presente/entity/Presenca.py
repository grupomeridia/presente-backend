#Roberto
from entity.PresencaEnum import TipoPresenca
from repository.PresencaRepository import PresencaRepository
import datetime

class Presenca(PresencaRepository.db.Model):
    __tablename__ = 'presencas'
    id = PresencaRepository.db.Column(PresencaRepository.db.Integer, primary_key=True)
    ativo = PresencaRepository.db.Column(PresencaRepository.db.Boolean, nullable=False)
    aluno_ra = PresencaRepository.db.Column(PresencaRepository.db.Integer, PresencaRepository.db.ForeignKey('alunos.ra'))
    turma_id = PresencaRepository.db.Column(PresencaRepository.db.Integer, PresencaRepository.db.ForeignKey('turmas.id'))
    projeto_id = PresencaRepository.db.Column(PresencaRepository.db.Integer, PresencaRepository.db.ForeignKey('projetos.id'))
    chamada_id = PresencaRepository.db.Column(PresencaRepository.db.Integer, PresencaRepository.db.ForeignKey('chamadas.id'))
    professor_id = PresencaRepository.db.Column(PresencaRepository.db.Integer, PresencaRepository.db.ForeignKey('professores.id'))
    tipo_presenca = PresencaRepository.db.Column(PresencaRepository.db.Enum(TipoPresenca))
    horario = PresencaRepository.db.Column(PresencaRepository.db.DateTime(timezone=True))

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
