from repository.MainRepository import MainRepository

class Configuracao(MainRepository.db.Model):
    id = MainRepository.db.Column(MainRepository.db.Integer, primary_key=True)
    ativo = MainRepository.db.Column(MainRepository.db.Boolean, nullable=False)
    turma_id = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('turma.id'))
    projeto_id = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('projeto.id'))

    def __init__(self, ativo:bool, turma:int, projeto:int):
        self.ativo = ativo
        self.turma_id = turma
        self.projeto_id = projeto
