from repository.MainRepository import MainRepository

class Materia(MainRepository.db.Model):
    __tablename__ = 'materias'
    id_materia = MainRepository.db.Column(MainRepository.db.Integer, primary_key=True)
    status = MainRepository.db.Column(MainRepository.db.Boolean, nullable=False)
    nome = MainRepository.db.Column(MainRepository.db.String(100), nullable=False)
    chamadas = MainRepository.db.relationship('Chamada', back_populates='materia')

    def __init__(self, status:bool, nome:str):
        self.status = status
        self.nome = nome
