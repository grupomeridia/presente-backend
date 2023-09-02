from repository.MainRepository import MainRepository

class Materia(MainRepository.db.Model):
    __tablename__ = 'materias'
    idMateria = MainRepository.db.Column(MainRepository.db.Integer, primary_key=True)
    status = MainRepository.db.Column(MainRepository.db.Boolean, nullable=False)
    nome = MainRepository.db.Column(MainRepository.db.String(100), nullable=False)
    chamadas = MainRepository.db.relationship('Chamada', back_populates='materia')

    def __init__(self, ativo:bool, nome:str):
        self.ativo = ativo
        self.nome = nome
