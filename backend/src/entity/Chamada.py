from repository.MainRepository import MainRepository
import datetime

class Chamada(MainRepository.db.Model):
    __tablename__ = 'chamadas'
    idChamada = MainRepository.db.Column(MainRepository.db.Integer, primaryKey=True)
    idMateria = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('materias.idMateria'))
    idTurma = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('turmas.idTurma'))
    idProfessor = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('professores.idProfessor'))
    status = MainRepository.db.Column(MainRepository.db.Boolean, nullable=False)
    abertura = MainRepository.db.Column(MainRepository.db.datetime, nullable=False)
    encerramento = MainRepository.db.Column(MainRepository.db.datetime)
    materia = MainRepository.db.relationship('Materia', back_populates='chamadas')
    turma = MainRepository.db.relationship('Turma', back_populates='chamadas')
    professor = MainRepository.db.relationship('Professor', back_populates='chamadas')
    presencas = MainRepository.db.relationship('Presenca', back_populates='chamada')
    
    def __init__(self, status:bool, abertura:datetime, encerramento:datetime):
        self.status = status
        self.abertura = abertura
        self.encerramento = encerramento


