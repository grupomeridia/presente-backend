from entity.PresencaEnum import TipoPresenca
from datetime import datetime
from pydantic import validate_arguments

class PresencaDTO:
    @validate_arguments
    def __init__(self, idAluno:int, idChamada:int, status:bool, tipoPresenca:TipoPresenca, horario:datetime):
        self.idAluno = idAluno
        self.idChamada = idChamada
        self.status = status
        self.tipoPresenca = tipoPresenca
        self.horario = horario