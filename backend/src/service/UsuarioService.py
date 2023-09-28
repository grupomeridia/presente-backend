from repository.UsuarioRepository import UsuarioRepository
from entity.Usuario import Usuario

class UsuarioService():
    def getUsuarioById(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("Deve ser um número inteiro")
        
        assert int(id) > 0, "ID inválido."
        assert UsuarioRepository.getUsuarioById(id) != None, "Nenhum usuario foi encontrado"

        return UsuarioRepository.getUsuarioById(id)
    
    def register(usuarioDto):
        
        usuario = UsuarioService.toEntity(usuarioDto)
        
        return UsuarioRepository.register(Usuario(idUsuario=usuario.idUsuario, status=usuario.status, login=usuario.login, senha=usuario.senha, cargo=usuario.cargo))
    
    def update(id, usuarioDto):
        
        usuario = UsuarioService.toEntity(usuarioDto)

        return UsuarioRepository.update(id, Usuario(usuario.status, usuario.login, usuario.senha, usuario.cargo)) 

    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro")

        assert int(id) > 0, "ID inválido"
        assert Usuario.query.filter(Usuario.id == id).first() is not None, "Usuario não encontrado" 
        return UsuarioRepository.delete(id)      

    def toEntity(usuarioDto):
        usuario = Usuario(idUsuario=usuarioDto.idUsuario, status=usuarioDto.status, login=usuarioDto.login, senha=usuarioDto.senha, cargo=usuarioDto.cargo)

        return usuario
