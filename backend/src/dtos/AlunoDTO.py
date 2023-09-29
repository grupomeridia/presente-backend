from pydantic import validate_arguments

class AlunoDTO:
    @validate_arguments
    def __init__(self, id_usuario:int, status:bool, ausente:bool, nome:str, ra:int):
        self.id_usuario = id_usuario
        self.status = status
        self.ausente = ausente
        self.nome = nome
        self.ra = ra