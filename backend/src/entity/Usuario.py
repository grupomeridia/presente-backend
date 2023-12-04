from entity.CargoEnum import Cargo
from models import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(id=user_id)

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.Boolean, nullable=False)
    login = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    ra = db.Column(db.Integer, unique=True)
    cargo = db.Column(db.Enum(Cargo))
    aluno = db.relationship('Aluno', uselist=False, back_populates='usuario')
    professor = db.relationship('Professor', uselist=False, back_populates='usuario')
    secretaria = db.relationship('Secretaria', uselist=False, back_populates='usuario')

    def __init__(self, status:bool, login:str, senha:str, nome:str, ra:int, cargo:Cargo):
        self.status = status
        self.login = login
        self.nome = nome
        self.ra = ra
        self.senha = generate_password_hash(senha)
        self.cargo = cargo

    def verifyPassword(password, given_password):
        return check_password_hash(password, given_password)
    
    def get_id(self):
           return (self.id_usuario)
    
