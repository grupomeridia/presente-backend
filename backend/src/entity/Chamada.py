from repository.MainRepository import MainRepository
import datetime

class Chamada(MainRepository.db.Model):
    __tablename__ = 'chamadas'
    idChamada = MainRepository.db.Column(MainRepository.db.Integer, primary_key=True)
    idMateria = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('materias.id_materia'))
    idTurma = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('turmas.id_turma'))
    idProfessor = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('professores.id_professor'))
    status = MainRepository.db.Column(MainRepository.db.Boolean, nullable=False)
    abertura = MainRepository.db.Column(MainRepository.db.DateTime, nullable=False)
    encerramento = MainRepository.db.Column(MainRepository.db.DateTime)
    materia = MainRepository.db.relationship('Materia', back_populates='chamadas')
    turma = MainRepository.db.relationship('Turma', back_populates='chamadas')
    professor = MainRepository.db.relationship('Professor', back_populates='chamadas')
    presencas = MainRepository.db.relationship('Presenca', back_populates='chamada')
    
    def __init__(self, idMateria:int, idTurma:int, idProfessor:int ,status:bool, abertura:datetime, encerramento:datetime):
        self.idMateria = idMateria
        self.idTurma = idTurma
        self.idProfessor = idProfessor
        self.status = status
        self.abertura = abertura
        self.encerramento = encerramento


