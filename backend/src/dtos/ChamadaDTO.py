from datetime import datetime
from pydantic import validate_arguments


class ChamadaDTO:
    @validate_arguments
    def __init__(self, status:bool, abertura:datetime, encerramento:datetime):
        self.status = status
        self.abertura = abertura
        self.encerramento = encerramento