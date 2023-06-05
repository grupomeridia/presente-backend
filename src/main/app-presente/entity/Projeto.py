from repository.ProjetoRepository import ProjetoRepository

class Projeto(ProjetoRepository.db.Model):
    __tablename__ = 'projetos'
    id = ProjetoRepository.db.Column(ProjetoRepository.db.Integer, primary_key=True)
    ativo = ProjetoRepository.db.Column(ProjetoRepository.db.Boolean, nullable=False)
    nome = ProjetoRepository.db.Column(ProjetoRepository.db.String, nullable=False)
    chamada = ProjetoRepository.db.relationship('chamadas', backref='projetos')
    presenca = ProjetoRepository.db.relationship('presencas', backref='projetos')
    configuracao = ProjetoRepository.db.relationship('configuracoes', backref='projetos')

    def __init__(self, id:int, ativo:bool, nome:str):
        self._id = id
        self._ativo = ativo
        self._nome = nome
