#hisham

from repository.ProfessorRepository import ProfessorRepository

class Professor(ProfessorRepository.db.Model):
    __tablename__ = 'professores'
    id = ProfessorRepository.db.Column(ProfessorRepository.db.Integer, primary_key=True)
    ativo = ProfessorRepository.db.Column(ProfessorRepository.db.Boolean, nullable=False)
    nome = ProfessorRepository.db.Clolumn(ProfessorRepository.db.String, nullable=False)

    # Validações
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


    # Metodos

    def verificaAlunos() -> bool:
        #IMPEDITIVO: Falta criar a classe controller
        #Esta função irá retornar os alunos presentes em sala.
        pass