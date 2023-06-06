from repository.MainRepository import MainRepository
from entity.Projeto import Projeto
from entity.Professor import Professor


class Chamada(MainRepository.db.Model):
    #__tablename__ = 'chamadas'
    id = MainRepository.db.Column(MainRepository.db.Integer, primary_key=True)
    ativo = MainRepository.db.Column(MainRepository.db.Boolean, nullable=False)
    projeto_id = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('projeto.id'))
    turma_id = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('turma.id'))
    professor_id = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('professor.id'))
    presenca = MainRepository.db.relationship('presenca', backref='chamada')

    def __init__(self, id:int, ativo:bool, projeto_id:int, turma_id:int, professor_id:int):
        self._id = id
        self._ativo = ativo
        self._projeto_id = projeto_id
        self._turma_id = turma_id
        self._professor_id = professor_id


