from entity.CargoEnum import Cargo
from models import db



class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id_usuario = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, nullable=False)
    login = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    cargo = db.Column(db.Enum(Cargo))
    aluno = db.relationship('Aluno', uselist=False, back_populates='usuario')
    professor = db.relationship('Professor', uselist=False, back_populates='usuario')
    secretaria = db.relationship('Secretaria', uselist=False, back_populates='usuario')

    def __init__(self, status:bool, login:str, senha:str, cargo:Cargo):
        self.status = status
        self.login = login
        self.senha = senha
        self.cargo = cargo