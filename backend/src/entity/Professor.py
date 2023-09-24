from repository.MainRepository import MainRepository

class Professor(MainRepository.db.Model):
    __tablename__ = 'professores'
    idProfessor = MainRepository.db.Column(MainRepository.db.Integer, primary_key=True)
    idUsuario = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('usuarios.idUsuario'))
    status = MainRepository.db.Column(MainRepository.db.Boolean, nullable=False)
    nome = MainRepository.db.Column(MainRepository.db.String(100), nullable=False)
    usuario = MainRepository.db.relationship('Usuario', back_populates='professor')
    chamadas = MainRepository.db.relationship('Chamada', back_populates='professor')
    turmas = MainRepository.db.relationship('Turma', secondary='turma_professor')

    def __init__(self, idUsuario:int, status:bool, nome:str):
        self.idUsuario = idUsuario
        self.status = status
        self.nome = nome
