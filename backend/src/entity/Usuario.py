from CargoEnum import Cargo
from repository.MainRepository import MainRepository



class Usuario(MainRepository.db.Model):
    __tablename__ = 'usuarios'
    idUsuario = MainRepository.db.Column(MainRepository.db.Integer, primary_key=True)
    status = MainRepository.db.Column(MainRepository.db.Boolean, nullable=False)
    login = MainRepository.db.Column(MainRepository.db.String(100), nullable=False)
    senha = MainRepository.db.Column(MainRepository.db.String(100), nullable=False)
    cargo = MainRepository.db.Column(MainRepository.db.Enum(Cargo))
    aluno = MainRepository.db.relationship('Aluno', uselist=False, back_populates='usuario')
    professor = MainRepository.db.relationship('Professor', uselist=False, back_populates='usuario')
    secretaria = MainRepository.db.relationship('Secretaria', uselist=False, back_populates='usuario')

    def __init__(self, status:bool, login:str, senha:str, cargo:Cargo):
        self.status = status
        self.login = login
        self.senha = senha
        self.cargo = cargo