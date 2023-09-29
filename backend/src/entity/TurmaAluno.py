from repository.MainRepository import MainRepository

turma_aluno = MainRepository.db.Table(
    'turma_aluno',
    MainRepository.db.Column('id_turma', MainRepository.db.Integer, MainRepository.db.ForeignKey('turmas.id_turma')),
    MainRepository.db.Column('id_aluno', MainRepository.db.Integer, MainRepository.db.ForeignKey('alunos.id_aluno'))
)