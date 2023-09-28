from entity.CargoEnum import Cargo
from datetime import datetime
from pydantic import validate_arguments

class LembreteDTO:
    @validate_arguments
    def __init__(self, destinatarioCargo:Cargo, titulo:str, mensagem:str, criacao:datetime, visualizacao:datetime):
        self.destinatarioCargo = destinatarioCargo
        self.titulo = titulo
        self.mensagem = mensagem
        self.criacao = criacao
        self.visualizacao = visualizacao