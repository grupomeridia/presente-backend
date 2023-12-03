from entity.PresencaEnum import TipoPresenca
from datetime import datetime
from pydantic import validate_arguments
from typing import Optional

class PresencaDTO:
    @validate_arguments
    def __init__(self, id_aluno:int, id_chamada:int, status:bool, tipo_presenca:TipoPresenca, cargo_manual:Optional[str], id_manual:Optional[int], horario:datetime):
        self.id_aluno = id_aluno
        self.id_chamada = id_chamada
        self.status = status
        self.tipo_presenca = tipo_presenca
        self.cargo_manual = cargo_manual
        self.id_manual = id_manual
        self.horario = horario