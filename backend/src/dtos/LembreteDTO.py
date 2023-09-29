from entity.CargoEnum import Cargo
from datetime import datetime
from pydantic import validate_arguments

class LembreteDTO:
    @validate_arguments
    def __init__(self, id_secretaria:int, destinatario_cargo:Cargo, destinatario_id:int, titulo:str, mensagem:str, criacao:datetime, visualizacao:datetime):
        self.id_secretaria = id_secretaria
        self.destinatario_cargo = destinatario_cargo
        self.destinatario_id = destinatario_id
        self.titulo = titulo
        self.mensagem = mensagem
        self.criacao = criacao
        self.visualizacao = visualizacao