from repository.MainRepository import MainRepository
import datetime

class Chamada(MainRepository.db.Model):
    __tablename__ = 'chamadas'
    id_chamada = MainRepository.db.Column(MainRepository.db.Integer, primary_key=True)
    id_materia = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('materias.id_materia'))
    id_turma = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('turmas.id_turma'))
    id_professor = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('professores.id_professor'))
    status = MainRepository.db.Column(MainRepository.db.Boolean, nullable=False)
    abertura = MainRepository.db.Column(MainRepository.db.DateTime, nullable=False)
    encerramento = MainRepository.db.Column(MainRepository.db.DateTime)
    materia = MainRepository.db.relationship('Materia', back_populates='chamadas')
    turma = MainRepository.db.relationship('Turma', back_populates='chamadas')
    professor = MainRepository.db.relationship('Professor', back_populates='chamadas')
    presencas = MainRepository.db.relationship('Presenca', back_populates='chamada')
    
    def __init__(self, id_materia:int, id_turma:int, id_professor:int ,status:bool, abertura:datetime, encerramento:datetime):
        self.id_materia = id_materia
        self.id_turma = id_turma
        self.id_professor = id_professor
        self.status = status
        self.abertura = abertura
        self.encerramento = encerramento


