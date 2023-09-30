from datetime import datetime
from pydantic import validate_arguments

class ConfiguracaoDTO:
    @validate_arguments
    def __init__(self, status:bool, aluno_ausente:int, inicio_aula:datetime, fim_aula:datetime):
        self.status = status
        self.aluno_ausente = aluno_ausente
        self.inicio_aula = inicio_aula
        self.fim_aula = fim_aula

