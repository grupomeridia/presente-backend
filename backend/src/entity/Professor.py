from models import db

class Professor(db.Model):
    __tablename__ = 'professores'
    id_professor = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'))
    status = db.Column(db.Boolean, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    usuario = db.relationship('Usuario', back_populates='professor')
    chamadas = db.relationship('Chamada', back_populates='professor')
    turmas = db.relationship('Turma', secondary='turma_professor')

    def __init__(self, id_usuario:int, status:bool, nome:str):
        self.id_usuario = id_usuario
        self.status = status
        self.nome = nome
