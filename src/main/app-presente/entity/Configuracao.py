from repository.ConfiguracaoRepository import ConfiguracaoRepository

class Configuracao(ConfiguracaoRepository.db.Model):
    __tablename__ = 'configuracoes'
    id = ConfiguracaoRepository.db.Column(ConfiguracaoRepository.db.Integer, primary_key=True)
    ativo = ConfiguracaoRepository.db.Column(ConfiguracaoRepository.db.Boolean, nullable=False)
    turma_id = ConfiguracaoRepository.db.Column(ConfiguracaoRepository.db.Integer, ConfiguracaoRepository.db.ForeignKey('turma.id'))
    projeto_integrador_id = ConfiguracaoRepository.db.Column(ConfiguracaoRepository.db.Integer, nullable=False)
    projeto_id = ConfiguracaoRepository.db.Column(ConfiguracaoRepository.db.Integer, ConfiguracaoRepository.db.ForeignKey('projeto.id'))

    def __init__(self, id:int, ativo:bool, turma_id=int, projeto_integrador_id=int, projeto_id=int):
        self._id = id
        self._ativo = ativo
        self._turma_id = turma_id
        self._projeto_integrador_id = projeto_integrador_id
        self._projeto_id = projeto_id
