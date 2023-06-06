from repository.TurmaRepository import TurmaRepository


class Turma(TurmaRepository.db.Model):
    __tablename__ ='turmas'
    id = TurmaRepository.db.Colum(TurmaRepository.db.Integer, primary_key = True)
    ativo = TurmaRepository.db.Column(TurmaRepository.db.Boolean, nullable=False)
    nome = TurmaRepository.db.Colum(TurmaRepository.db.String(50), nullable=False)
    ano = TurmaRepository.db.Colum(TurmaRepository.db.Integer, nullable=False)
    semestre = TurmaRepository.db.Colum(TurmaRepository.db.String(1), nullalbe=False)
    chamada = TurmaRepository.db.relationship('chamadas', backref='turmas')
    presenca = TurmaRepository.db.relationship('presencas', backref='turmas')


    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        if(isinstance(value, int) and value > 0):
            self._id = value
        else:
            raise ValueError("ID incorreto, deve ser um número maior que zero")
        
    @id.deleter
    def id(self):
        self._id = None

    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, value:str):
        if(isinstance(value, str) and len(value) > 3):
            self._nome = value
        else:
            raise Exception("Nome inválido!")
    
    @nome.deleter
    def nome(self):
        self._nome = None


    def __init__(self, id:int, nome: str , ano : int, semestre : int):
        self.id = id
        self.nome = nome
        self.ano = ano
        self.semestre = semestre
