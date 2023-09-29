from entity.PresencaEnum import TipoPresenca
from datetime import datetime
from pydantic import validate_arguments

class PresencaDTO:
    @validate_arguments
    def __init__(self, id_aluno:int, id_chamada:int, status:bool, tipo_presenca:TipoPresenca, horario:datetime):
        self.id_aluno = id_aluno
        self.id_chamada = id_chamada
        self.status = status
        self.tipo_presenca = tipo_presenca
        self.horario = horario