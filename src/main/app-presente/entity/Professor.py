#hisham

class Professor():
    def __init__(self, id, nome) -> None:
        self._id = id
        self._nome = nome

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