from repository.UsuarioRepository import UsuarioRepository
from entity.Usuario import Usuario

class UsuarioService():
    @staticmethod
    def get_usuario_by_id(id):
        
        assert int(id) > 0, "ID inválido."
        assert UsuarioRepository.get_usuario_by_id(id) != None, "Nenhum usuario foi encontrado"

        return UsuarioRepository.get_usuario_by_id(id)
    
    @staticmethod
    def register(usuario_dto):
        
        usuario = UsuarioService.to_entity(usuario_dto)
        
        assert not Usuario.query.filter(Usuario.login == usuario.login).first(), "Esse login já está sendo usado"

        return UsuarioRepository.register(Usuario(status=usuario.status, login=usuario.login, senha=usuario.senha, cargo=usuario.cargo))
    
    @staticmethod
    def update(id, usuario_dto):
        
        usuario = UsuarioService.to_entity(usuario_dto)

        return UsuarioRepository.update(id, Usuario(status=usuario.status, login=usuario.login, senha=usuario.senha, cargo=usuario.cargo)) 

    @staticmethod
    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro")

        assert int(id) > 0, "ID inválido"
        assert Usuario.query.filter(Usuario.id_usuario == id).first() is not None, "Usuario não encontrado" 
        return UsuarioRepository.delete(id)      

    @staticmethod
    def to_entity(usuario_dto):
        usuario = Usuario(status=usuario_dto.status, login=usuario_dto.login, senha=usuario_dto.senha, cargo=usuario_dto.cargo)

        return usuario
