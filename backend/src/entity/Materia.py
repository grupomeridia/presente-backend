from models import db

class Materia(db.Model):
    __tablename__ = 'materias'
    id_materia = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    chamadas = db.relationship('Chamada', back_populates='materia')

    def __init__(self, status:bool, nome:str):
        self.status = status
        self.nome = nome
