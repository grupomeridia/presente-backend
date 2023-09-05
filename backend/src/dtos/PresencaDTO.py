from PresencaEnum import TipoPresenca
import datetime
class PresencaDTO:
    def __init__(self, status:bool, tipoPresenca:TipoPresenca, horario:datetime):
        self.status = status
        self.tipoPresenca = tipoPresenca
        self.horario = horario