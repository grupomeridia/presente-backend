from models import db


class Aluno(db.Model):
    __tablename__ = 'alunos'
    id_aluno = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'))
    status = db.Column(db.Boolean, nullable=False)
    ausente = db.Column(db.Boolean, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    ra = db.Column(db.Integer, nullable=False, unique=True)
    usuario = db.relationship('Usuario', back_populates='aluno')
    presencas = db.relationship('Presenca', back_populates='aluno')
    turmas = db.relationship('Turma', secondary='turma_aluno')    

    def __init__(self, id_usuario:int, status:bool, ausente:bool, nome:str, ra:int):
        self.id_usuario = id_usuario
        self.status = status
        self.ausente = ausente
        self.nome = nome
        self.ra = ra
        



