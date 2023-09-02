from repository.MainRepository import MainRepository

class Painel(MainRepository.db.Model):
    __tablename__ = 'configuracoes'
    idPainel = MainRepository.db.Column(MainRepository.db.Integer, primary_key=True)
    idConfiguracao = MainRepository.db.Column(MainRepository.db.ForeignKey('configuracoes.idConfiguracao'))
    idSecretaria = MainRepository.db.Column(MainRepository.db.ForegnKey('secretaria.idSecretaria'))
    data = MainRepository.db.Column(MainRepository.db.datetime, nullable=False)
    totalAtivos = MainRepository.db.Column(MainRepository.db.Integer, nullable=False)
    totalPresentes = MainRepository.db.Column(MainRepository.db.Integer, nullable=False)
    totalAusentes = MainRepository.db.Column(MainRepository.db.Integer, nullable=False)
    totalPresentesCurso = list
    totalAtivoCurso = list
    totalAUsenteCurso = list
    configuracao = MainRepository.db.relationship('Configuracao', back_populates='painel')
    secretaria = MainRepository.db.relationship('Secretaria', back_populates='painel')