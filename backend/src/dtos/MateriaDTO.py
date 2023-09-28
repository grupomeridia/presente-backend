from pydantic import validate_arguments

class MateriaDTO:
    @validate_arguments
    def __init__(self, status:bool, nome:str):
        self.status = status
        self.nome = nome