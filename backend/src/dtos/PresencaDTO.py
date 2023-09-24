from entity.PresencaEnum import TipoPresenca
import datetime
class PresencaDTO:
    def __init__(self, idAluno:int, idChamada:int, status:bool, tipoPresenca:TipoPresenca, horario:datetime):
        self.idAluno = idAluno
        self.idChamada = idChamada
        self.status = status
        self.tipoPresenca = tipoPresenca
        self.horario = horario