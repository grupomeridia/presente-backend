import datetime
from pydantic import validade_arguments


class ChamadaDTO:
    @validade_arguments
    def __init__(self, status:bool, abertura:datetime, encerramento:datetime):
        self.status = status
        self.abertura = abertura
        self.encerramento = encerramento