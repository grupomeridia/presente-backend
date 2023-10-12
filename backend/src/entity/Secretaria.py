from models import db

class Secretaria(db.Model):
    __tablename__ = 'secretaria'
    id_secretaria = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'))
    status = db.Column(db.Boolean, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    usuario = db.relationship('Usuario', back_populates='secretaria')
    lembrete = db.relationship('Lembrete', back_populates='secretaria')
    painel = db.relationship('Painel', back_populates='secretaria')

    def __init__(self, id_usuario:int, status:bool, nome:str):
        self.id_usuario = id_usuario
        self.status = status
        self.nome = nome