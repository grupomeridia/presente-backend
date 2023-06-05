from repository.ChamadaRepository import ChamadaRepository


class Chamada(ChamadaRepository.db.Model):
    __tablename__ = 'chamadas'
    id = ChamadaRepository.db.Column(ChamadaRepository.db.Integer, primary_key=True)
    ativo = ChamadaRepository.db.Column(ChamadaRepository.db.Boolean, nullable=False)
    projeto_id = ChamadaRepository.db.Column(ChamadaRepository.db.Integer, ChamadaRepository.db.ForeignKey('projetos.id'))
    turma_id = ChamadaRepository.db.Column(ChamadaRepository.db.Integer, ChamadaRepository.db.ForeignKey('turmas.id'))
    professor_id = ChamadaRepository.db.Column(ChamadaRepository.db.Integer, ChamadaRepository.db.ForeignKey('professores.id'))
    presenca = ChamadaRepository.db.relationship('presencas', backref='chamadas')

    def __init__(self, id:int, ativo:bool, projeto_id:int, turma_id:int, professor_id:int):
        self._id = id
        self._ativo = ativo
        self._projeto_id = projeto_id
        self._turma_id = turma_id
        self._professor_id = professor_id


