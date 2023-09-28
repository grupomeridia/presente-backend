from pydantic import validate_arguments

class ProfessorDTO:
    @validate_arguments
    def __init__(self, id_usuario:int, status:bool, nome:str):
        self.id_usuario = id_usuario
        self.status = status
        self.nome = nome