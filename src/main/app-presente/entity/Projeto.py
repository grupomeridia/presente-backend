from repository.MainRepository import MainRepository
from entity.Chamada import Chamada

class Projeto(MainRepository.db.Model):
    #__tablename__ = 'projetos'
    id = MainRepository.db.Column(MainRepository.db.Integer, primary_key=True)
    ativo = MainRepository.db.Column(MainRepository.db.Boolean, nullable=False)
    nome = MainRepository.db.Column(MainRepository.db.String, nullable=False)
    chamada = MainRepository.db.relationship('chamada', backref='projeto')
    presenca = MainRepository.db.relationship('presenca', backref='projeto')
    configuracao = MainRepository.db.relationship('configuracao', backref='projeto')

    def __init__(self, id:int, ativo:bool, nome:str):
        self._id = id
        self._ativo = ativo
        self._nome = nome
