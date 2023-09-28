from entity.CargoEnum import Cargo
from pydantic import validate_arguments

class UsuarioDTO:
    @validate_arguments
    def __init__(self, idUsuario:int, status:bool, login:str, senha:str, cargo:Cargo):
        self.idUsuario = idUsuario
        self.status = status
        self.login = login
        self.senha = senha
        self.cargo = cargo