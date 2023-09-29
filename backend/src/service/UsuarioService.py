from repository.UsuarioRepository import UsuarioRepository
from entity.Usuario import Usuario

class UsuarioService():
    def getUsuarioById(id):
        
        assert int(id) > 0, "ID inválido."
        assert UsuarioRepository.getUsuarioById(id) != None, "Nenhum usuario foi encontrado"

        return UsuarioRepository.getUsuarioById(id)
    
    def register(usuarioDto):
        
        usuario = UsuarioService.toEntity(usuarioDto)
        
        assert not Usuario.query.filter(Usuario.login == usuario.login).first(), "Esse login já está sendo usado"

        return UsuarioRepository.register(Usuario(status=usuario.status, login=usuario.login, senha=usuario.senha, cargo=usuario.cargo))
    
    def update(id, usuarioDto):
        
        usuario = UsuarioService.toEntity(usuarioDto)

        return UsuarioRepository.update(id, Usuario(status=usuario.status, login=usuario.login, senha=usuario.senha, cargo=usuario.cargo)) 

    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro")

        assert int(id) > 0, "ID inválido"
        assert Usuario.query.filter(Usuario.id_usuario == id).first() is not None, "Usuario não encontrado" 
        return UsuarioRepository.delete(id)      

    def toEntity(usuarioDto):
        usuario = Usuario(status=usuarioDto.status, login=usuarioDto.login, senha=usuarioDto.senha, cargo=usuarioDto.cargo)

        return usuario
