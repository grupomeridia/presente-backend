from repository.MainRepository import MainRepository

class Configuracao(MainRepository.db.Model):
    __tablename__ = 'configuracoes'
    idConfiguracao = MainRepository.db.Column(MainRepository.db.Integer, primary_key=True)
    status = MainRepository.db.Column(MainRepository.db.Boolean, nullable=False)
    alunoAusente = MainRepository.db.Column(MainRepository.db.Integer, nullable=False)
    inicioAula = MainRepository.db.Column(MainRepository.db.datetime, nullable=False)
    finalAula = MainRepository.db.Column(MainRepository.db.datetime, nullable=False)
    painel = MainRepository.db.relationship('Painel', back_populates='configuracao')

    def __init__(self, status, alunoAusente, inicioAula, finalAula):
        self.status = status
        self.alunoAusente = alunoAusente
        self.inicioAula = inicioAula
        self.finalAula = finalAula

