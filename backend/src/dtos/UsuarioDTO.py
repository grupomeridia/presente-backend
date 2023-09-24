from entity.CargoEnum import Cargo

class UsuarioDTO:
    def __init__(self, status:bool, login:str, senha:str, cargo:Cargo):
        self.status = status
        self.login = login
        self.senha = senha
        self.cargo = cargo