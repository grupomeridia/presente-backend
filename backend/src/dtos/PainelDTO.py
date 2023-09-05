import datetime

class PainelDTO:
    def __init__(self, data:datetime, totalAtivos:int, totalPresentes:int, totalAusentes:int, totalPresentesCurso:list, totalAtivoCurso:list, totalAusenteCurso:list):
        self.data = data
        self.totalAtivos = totalAtivos
        self.totalPresentes = totalPresentes
        self.totalAusentes = totalAusentes
        self.totalPresentesCurso = totalPresentesCurso
        self.totalAtivoCurso = totalAtivoCurso
        self.totalAusenteCurso = totalAusenteCurso