from repository.MainRepository import MainRepository

class Secretaria(MainRepository.db.Model):
    __tablename__ = 'secretaria'
    id_secretaria = MainRepository.db.Column(MainRepository.db.Integer, primary_key=True)
    id_usuario = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('usuarios.id_usuario'))
    status = MainRepository.db.Column(MainRepository.db.Boolean, nullable=False)
    nome = MainRepository.db.Column(MainRepository.db.String(100), nullable=False)
    usuario = MainRepository.db.relationship('Usuario', back_populates='secretaria')
    lembrete = MainRepository.db.relationship('Lembrete', back_populates='secretaria')
    painel = MainRepository.db.relationship('Painel', back_populates='secretaria')

    def __init__(self, id_usuario:int, status:bool, nome:str):
        self.id_usuario = id_usuario
        self.status = status
        self.nome = nome