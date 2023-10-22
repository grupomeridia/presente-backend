from entity.CargoEnum import Cargo
from pydantic import validate_arguments
from typing import Optional

class UsuarioDTO:
    @validate_arguments
    def __init__(self, status:bool, login:str, senha:str, nome:str, ra:Optional[int], cargo:Cargo):
        self.status = status
        self.login = login
        self.senha = senha
        self.nome = nome
        self.ra = ra
        self.cargo = cargo