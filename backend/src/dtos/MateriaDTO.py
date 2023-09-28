from pydantic import validate_arguments

class MateriaDTO:
    @validate_arguments
    def __init__(self, ativo:bool, nome:str):
        self.ativo = ativo
        self.nome = nome