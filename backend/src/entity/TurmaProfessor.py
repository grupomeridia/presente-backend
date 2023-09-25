from repository.MainRepository import MainRepository

turma_professor = MainRepository.db.Table(
    'turma_professor',
    MainRepository.db.Column('id_turma', MainRepository.db.Integer, MainRepository.db.ForeignKey('turmas.idTurma')),
    MainRepository.db.Column('id_professor', MainRepository.db.Integer, MainRepository.db.ForeignKey('professores.idProfessor'))
)