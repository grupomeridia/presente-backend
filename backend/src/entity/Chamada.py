from repository.MainRepository import MainRepository

from entity.Presenca import Presenca

class Chamada(MainRepository.db.Model):
    #__tablename__ = 'chamadas'
    id = MainRepository.db.Column(MainRepository.db.Integer, primary_key=True)
    ativo = MainRepository.db.Column(MainRepository.db.Boolean, nullable=False)
    projeto_id = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('projeto.id'))
    turma_id = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('turma.id'))
    professor_id = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('professor.id'))
    presenca = MainRepository.db.relationship('Presenca', backref='chamada')
    

    def __init__(self, ativo:bool, projeto:int, turma:int, professor:int):
        self.ativo = ativo
        self.projeto_id = projeto
        self.turma_id = turma
        self.professor_id = professor


