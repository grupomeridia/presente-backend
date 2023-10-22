from entity.CargoEnum import Cargo
from models import db



class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.Boolean, nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    ra = db.Column(db.Integer, unique=True)
    cargo = db.Column(db.Enum(Cargo))
    aluno = db.relationship('Aluno', uselist=False, back_populates='usuario')
    professor = db.relationship('Professor', uselist=False, back_populates='usuario')
    secretaria = db.relationship('Secretaria', uselist=False, back_populates='usuario')

    def __init__(self, status:bool, username:str, password:str, nome:str, ra:int, cargo:Cargo):
        self.status = status
        self.username = username
        self.password = password
        self.nome = nome
        self.ra = ra
        self.cargo = cargo