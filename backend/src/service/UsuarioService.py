from repository.UsuarioRepository import UsuarioRepository

from entity.Usuario import Usuario
from entity.CargoEnum import Cargo

from dtos.UsuarioDTO import UsuarioDTO

import re

class UsuarioService():
    @staticmethod
    def get_usuario_by_id(id):
        assert id != None, "Nenhum ID enviado."
        assert int(id) if isinstance(id, (int,str)) and id.isdigit() else None, "ID incorreto."
        assert int(id) > 0 and int(id) < 999999, "ID inválido."
        assert Usuario.query.get(id) != None, "Nenhum usuário com este ID foi encontrado."
    
        return UsuarioRepository.get_usuario_by_id(id)
    
    @staticmethod
    def register(status, login, senha, cargo):     

        assert login != 'NOT_FOUND', "Campo 'login' inexistente."
        assert cargo != 'NOT_FOUND', "Campo 'cargo' inexistente."
        assert senha != 'NOT_FOUND', "Campo 'senha' inexistente."

        cargos = [x.value for x in Cargo]
        assert cargo in cargos, "Cargo inválido"

        assert len(login) > 3, "Login com tamanho inválido."
        assert login.isalpha(), "O Login deve conter apenas letras."

        assert len(senha) > 6, "Tamanho de senha mínimo não atingido."
        assert not re.match(r'^[a-zA-Z]+$', senha), "Senha deve conter números, letras maiúsculas e caractéres especiais."

        assert not Usuario.query.filter(Usuario.login ==login).first(), "Esse login já está sendo usado"
        
        usuario = UsuarioService.to_entity(UsuarioDTO(status=status, login=login, senha=senha, cargo=cargo))
        return UsuarioRepository.register(usuario)
    
    @staticmethod
    def update(id_usuario, status, login, senha, cargo):      

        assert login != 'NOT_FOUND', "Campo 'login' inexistente."
        assert cargo != 'NOT_FOUND', "Campo 'cargo' inexistente."
        assert senha != 'NOT_FOUND', "Campo 'senha' inexistente."

        assert len(login) > 3, "Login com tamanho inválido."
        assert login.isalpha(), "O Login deve conter apenas letras."

        assert len(senha) > 6, "Tamanho de senha mínimo não atingido."
        assert not re.match(r'^[a-zA-Z]+$', senha), "Senha deve conter números, letras maiúsculas e caractéres especiais."
        

        usuario = UsuarioService.to_entity(UsuarioDTO(status=status, login=login, senha=senha, cargo=cargo))

        return UsuarioRepository.update(id_usuario, usuario) 

    @staticmethod
    def delete(id):
        
        assert int(id) if isinstance(id, (int,str)) and id.isdigit() else None, "ID incorreto."
        assert int(id) > 0 and int(id) < 999999, "ID inválido"
        assert Usuario.query.filter(Usuario.id_usuario == id).first() is not None, "Usuario não encontrado" 
        return UsuarioRepository.delete(id)      


    @staticmethod
    def to_entity(usuario_dto):
        usuario = Usuario(status=usuario_dto.status, login=usuario_dto.login, senha=usuario_dto.senha, cargo=usuario_dto.cargo)
        return usuario
