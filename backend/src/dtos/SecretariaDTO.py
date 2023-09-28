from pydantic import validate_arguments

class SecretariaDTO:
    @validate_arguments
    def __init__(self, idUsuario:int, status:bool, nome:str):
        self.idUsuario = idUsuario
        self.status = status
        self.nome = nome