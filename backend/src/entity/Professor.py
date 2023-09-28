from repository.MainRepository import MainRepository

class Professor(MainRepository.db.Model):
    __tablename__ = 'professores'
    id_professor = MainRepository.db.Column(MainRepository.db.Integer, primary_key=True)
    id_usuario = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('usuarios.id_usuario'))
    status = MainRepository.db.Column(MainRepository.db.Boolean, nullable=False)
    nome = MainRepository.db.Column(MainRepository.db.String(100), nullable=False)
    usuario = MainRepository.db.relationship('Usuario', back_populates='professor')
    chamadas = MainRepository.db.relationship('Chamada', back_populates='professor')
    turmas = MainRepository.db.relationship('Turma', secondary='turma_professor')

    def __init__(self, id_usuario:int, status:bool, nome:str):
        self.id_usuario = id_usuario
        self.status = status
        self.nome = nome
