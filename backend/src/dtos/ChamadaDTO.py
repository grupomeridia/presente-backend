from datetime import datetime
from pydantic import validate_arguments


class ChamadaDTO:
    @validate_arguments
    def __init__(self, id_materia:int, id_turma:int, id_professor:int, status:bool, abertura:datetime, encerramento:datetime):
        self.id_materia = id_materia
        self.id_turma = id_turma
        self.id_professor = id_professor
        self.status = status
        self.abertura = abertura
        self.encerramento = encerramento