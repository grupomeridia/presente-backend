from datetime import datetime
from pydantic import validate_arguments

class PainelDTO:
    @validate_arguments
    def __init__(self, id_configuracao:int, id_secretaria:int, data_criado:datetime, total_ativo:int, total_presentes:int, total_ausentes:int, total_presentes_curso:int, total_ativo_curso:int, total_ausente_curso:int):
        self.id_configuracao = id_configuracao
        self.id_secretaria = id_secretaria
        self.data_criado = data_criado
        self.total_ativo = total_ativo
        self.total_presentes = total_presentes
        self.total_ausentes = total_ausentes
        self.total_presentes_curso = total_presentes_curso
        self.total_ativo_curso = total_ativo_curso
        self.total_ausente_curso = total_ausente_curso