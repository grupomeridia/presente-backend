from repository.MainRepository import MainRepository

class Secretaria(MainRepository.db.Model):
    __tablename__ = 'secretaria'
    idSecretaria = MainRepository.db.Column(MainRepository.db.Integer, primary_key=True)
    idUsuario = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('usuarios.idUsuario'))
    status = MainRepository.db.Column(MainRepository.db.Boolean, nullable=False)
    nome = MainRepository.db.Column(MainRepository.db.String(100), nullable=False)
    usuario = MainRepository.db.relationship('Usuario', back_populates='secretaria')
    lembrete = MainRepository.db.relationship('Lembrete', back_populates='secretaria')
    painel = MainRepository.db.relationship('Painel', back_populates='secretaria')

    def __init__(self, idUsuario:int, status:bool, nome:str):
        self.idUsuario = idUsuario
        self.status = status
        self.nome = nome