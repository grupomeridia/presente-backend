from pydantic import validade_arguments

class AlunoDTO:
    @validade_arguments
    def __init__(self, status:bool, ausente:bool, nome:str, ra:int):
        self.status = status
        self.ausente = ausente
        self.nome = nome
        self.ra = ra