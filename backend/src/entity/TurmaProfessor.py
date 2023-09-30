from models import db

turma_professor = db.Table(
    'turma_professor',
    db.Column('id_turma', db.Integer, db.ForeignKey('turmas.id_turma')),
    db.Column('id_professor', db.Integer, db.ForeignKey('professores.id_professor'))
)