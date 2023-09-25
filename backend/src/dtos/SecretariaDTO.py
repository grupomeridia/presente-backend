from pydantic import validade_arguments

class SecretariaDTO:
    @validade_arguments
    def __init__(self, idUsuario:int, status:bool, nome:str):
        self.idUsuario = idUsuario
        self.status = status
        self.nome = nome