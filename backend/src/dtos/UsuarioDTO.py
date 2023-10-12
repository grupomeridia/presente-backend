from entity.CargoEnum import Cargo
from pydantic import validate_arguments

class UsuarioDTO:
    @validate_arguments
    def __init__(self, status:bool, login:str, senha:str, cargo:Cargo):
        self.status = status
        self.login = login
        self.senha = senha
        self.cargo = cargo