from CargoEnum import Cargo
import datetime
from pydantic import validade_arguments

class LembreteDTO:
    @validade_arguments
    def __init__(self, destinatarioCargo:Cargo, titulo:str, mensagem:str, criacao:datetime, visualizacao:datetime):
        self.destinatarioCargo = destinatarioCargo
        self.titulo = titulo
        self.mensagem = mensagem
        self.criacao = criacao
        self.visualizacao = visualizacao