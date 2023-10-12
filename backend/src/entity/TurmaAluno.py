from models import db

turma_aluno = db.Table(
    'turma_aluno',
    db.Column('id_turma', db.Integer, db.ForeignKey('turmas.id_turma')),
    db.Column('id_aluno', db.Integer, db.ForeignKey('alunos.id_aluno'))
)