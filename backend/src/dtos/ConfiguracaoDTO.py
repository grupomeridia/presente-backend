from datetime import datetime
from pydantic import validate_arguments

class ConfiguracaoDTO:
    @validate_arguments
    def __init__(self, status:bool, aluno_ausente:bool, inicio_aula:datetime, final_aula:datetime):
        self.status = status
        self.aluno_ausente = aluno_ausente
        self.inicio_aula = inicio_aula
        self.final_aula = final_aula