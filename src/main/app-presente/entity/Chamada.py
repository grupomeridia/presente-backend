#Roberto

from ControllerSqlAlchemy import db


class Chamada():
    __tablename__ = 'chamadas'
    id = db.Column(db.Integer, primary_key=True)
    ativo = db.Column(db.Boolean, nullable=False)
    projeto_id = db.Column(db.Integer, db.ForeignKey('projetos.id'))
    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'))
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'))
    presenca = db.relationship('Presenca', backref='chamada')

    def __init__(self, id, ativo, projeto_id, turma_id, professor_id):
        self.id = id
        self.ativo = ativo
        self.projeto_id = projeto_id
        self.turma_id = turma_id
        self.professor_id = professor_id


