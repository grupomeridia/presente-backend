import datetime
from pydantic import validade_arguments

class ConfiguracaoDTO:
    @validade_arguments
    def __init__(self, status:bool, alunoAusente:bool, inicioAula:datetime, finalAula:datetime):
        self.status = status
        self.alunoAusente = alunoAusente
        self.inicioAula = inicioAula
        self.finalAula = finalAula