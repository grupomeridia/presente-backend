from repository.MainRepository import MainRepository

from entity.Chamada import Chamada
from entity.Presenca import Presenca

class Professor(MainRepository.db.Model):
    #__tablename__ = 'professores'
    id = MainRepository.db.Column(MainRepository.db.Integer, primary_key=True)
    ativo = MainRepository.db.Column(MainRepository.db.Boolean, nullable=False)
    nome = MainRepository.db.Column(MainRepository.db.String, nullable=False)
    presenca = MainRepository.db.relationship('Presenca', backref='professor')
    chamada = MainRepository.db.relationship('Chamada', backref='professor')

    def verificaAlunos() -> bool:
        #IMPEDITIVO: Falta criar a classe controller
        #Esta função irá retornar os alunos presentes em sala.
        pass