from pydantic import validade_arguments

class MateriaDTO:
    @validade_arguments
    def __init__(self, ativo:bool, nome:str):
        self.ativo = ativo
        self.nome = nome