from datetime import datetime
from pydantic import validate_arguments
from typing import Optional

class ChamadaDTO:
    @validate_arguments
    def __init__(self, id_turma:int, id_professor:int, status:bool, abertura:datetime, encerramento: Optional[datetime] = None):
        self.id_turma = id_turma
        self.id_professor = id_professor
        self.status = status
        self.abertura = abertura
        self.encerramento = encerramento