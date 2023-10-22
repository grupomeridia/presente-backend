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
    def register(status, username, password, nome, ra, cargo):     

        assert username != 'NOT_FOUND', "Campo 'username' inexistente."
        assert cargo != 'NOT_FOUND', "Campo 'cargo' inexistente."
        assert password != 'NOT_FOUND', "Campo 'senha' inexistente."
        assert nome != 'NOT_FOUND', "Campo 'nome' inexistente."


        cargos = [x.value for x in Cargo]
        assert cargo in cargos, "Cargo inválido"

        assert len(username) > 3, "username com tamanho inválido."
        assert username.isalpha(), "O username deve conter apenas letras."

        assert len(password) > 6, "Tamanho de password mínimo não atingido."
        assert not re.match(r'^[a-zA-Z]+$', password), "password deve conter números, letras maiúsculas e caractéres especiais."

        assert len(nome) > 2, "nome com tamanho inválido."

        assert not Usuario.query.filter(Usuario.username == username).first(), "Esse username já está sendo usado"
        
        if (cargo != "Aluno"):
                    ra = None

        usuario = UsuarioService.to_entity(UsuarioDTO(status=status, username=username, password=password, nome=nome, ra=ra, cargo=cargo))
        
        return UsuarioRepository.register(usuario)
    
    @staticmethod
    def update(id_usuario, status, username, password, nome, ra, cargo):      

        assert username != 'NOT_FOUND', "Campo 'username' inexistente."
        assert cargo != 'NOT_FOUND', "Campo 'cargo' inexistente."
        assert password != 'NOT_FOUND', "Campo 'password' inexistente."
        assert nome != 'NOT_FOUND', "Campo 'nome' inexistente."

        assert len(username) > 3, "username com tamanho inválido."
        assert username.isalpha(), "O username deve conter apenas letras."

        assert len(password) > 6, "Tamanho de password mínimo não atingido."
        assert not re.match(r'^[a-zA-Z]+$', password), "password deve conter números, letras maiúsculas e caractéres especiais."
        
        assert len(nome) > 2, "nome com tamanho inválido."

        if (cargo != "Aluno"):
            ra = None

        usuario = UsuarioService.to_entity(UsuarioDTO(status=status, username=username, password=password, nome=nome, ra=ra, cargo=cargo))

        return UsuarioRepository.update(id_usuario, usuario) 

    @staticmethod
    def delete(id):
        
        assert int(id) if isinstance(id, (int,str)) and id.isdigit() else None, "ID incorreto."
        assert int(id) > 0 and int(id) < 999999, "ID inválido"
        assert Usuario.query.filter(Usuario.id_usuario == id).first() is not None, "Usuario não encontrado" 
        return UsuarioRepository.delete(id)      


    @staticmethod
    def to_entity(usuario_dto):
        usuario = Usuario(status=usuario_dto.status, username=usuario_dto.username, password=usuario_dto.password, nome=usuario_dto.nome, ra=usuario_dto.ra, cargo=usuario_dto.cargo)       
        
        return usuario
