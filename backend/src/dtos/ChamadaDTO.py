import datetime

class ChamadaDTO:
    def __init__(self, status:bool, abertura:datetime, encerramento:datetime):
        self.status = status
        self.abertura = abertura
        self.encerramento = encerramento