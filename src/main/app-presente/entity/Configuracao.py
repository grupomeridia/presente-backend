from repository.MainRepository import MainRepository

class Configuracao(MainRepository.db.Model):
    #__tablename__ = 'configuracoes'
    id = MainRepository.db.Column(MainRepository.db.Integer, primary_key=True)
    ativo = MainRepository.db.Column(MainRepository.db.Boolean, nullable=False)
    turma_id = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('turma.id'))
    projeto_integrador_id = MainRepository.db.Column(MainRepository.db.Integer, nullable=False)
    projeto_id = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('projeto.id'))

    def __init__(self, id:int, ativo:bool, turma=int, projeto_integrador=int, projeto=int):
        self.id = id
        self.ativo = ativo
        self.turma_id = turma
        self.projeto_integrador_id = projeto_integrador
        self.projeto_id = projeto
