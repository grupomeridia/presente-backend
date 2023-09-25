from entity.CargoEnum import Cargo
from pydantic import validade_arguments

class UsuarioDTO:
    @validade_arguments
    def __init__(self, status:bool, login:str, senha:str, cargo:Cargo):
        self.status = status
        self.login = login
        self.senha = senha
        self.cargo = cargo