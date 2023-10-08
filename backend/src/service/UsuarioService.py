from repository.UsuarioRepository import UsuarioRepository
from entity.Usuario import Usuario
import re

class UsuarioService():
    @staticmethod
    def get_usuario_by_id(id):
        assert id != None, "Nenhum ID enviado."
        assert int(id) if isinstance(id, (int,str)) and id.isdigit() else None, "ID incorreto."
        assert int(id) > 0 and int(id) < 999999, "ID inválido."
    
        return UsuarioRepository.get_usuario_by_id(id)
    
    @staticmethod
    def register(usuario_dto):
        
        usuario = UsuarioService.to_entity(usuario_dto)

        assert usuario.login != 'NOT_FOUND', "Campo 'login' inexistente."
        assert usuario.cargo != 'NOT_FOUND', "Campo 'cargo' inexistente."
        assert usuario.senha != 'NOT_FOUND', "Campo 'senha' inexistente."

        assert len(usuario.login) > 3, "Login com tamanho inválido."
        assert usuario.login.isalpha(), "O Login deve conter apenas letras."

        assert len(usuario.senha) > 6, "Tamanho de senha mínimo não atingido."
        assert not re.match(r'^[a-zA-Z]+$', usuario.senha), "Senha deve conter números, letras maiúsculas e caractéres especiais."

        assert not Usuario.query.filter(Usuario.login == usuario.login).first(), "Esse login já está sendo usado"

        return UsuarioRepository.register(Usuario(status=usuario.status, login=usuario.login, senha=usuario.senha, cargo=usuario.cargo))
    
    @staticmethod
    def update(id, usuario_dto):
        
        usuario = UsuarioService.to_entity(usuario_dto)

        assert usuario.login != 'NOT_FOUND', "Campo 'login' inexistente."
        assert usuario.cargo != 'NOT_FOUND', "Campo 'cargo' inexistente."
        assert usuario.senha != 'NOT_FOUND', "Campo 'senha' inexistente."

        assert len(usuario.login) > 3, "Login com tamanho inválido."
        assert usuario.login.isalpha(), "O Login deve conter apenas letras."

        assert len(usuario.senha) > 6, "Tamanho de senha mínimo não atingido."
        assert not re.match(r'^[a-zA-Z]+$', usuario.senha), "Senha deve conter números, letras maiúsculas e caractéres especiais."

        assert not Usuario.query.filter(Usuario.login == usuario.login).first(), "Esse login já está sendo usado"


        return UsuarioRepository.update(id, Usuario(status=usuario.status, login=usuario.login, senha=usuario.senha, cargo=usuario.cargo)) 

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
