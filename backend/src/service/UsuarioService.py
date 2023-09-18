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
    
    def register(status, login, senha, cargo):
        try:
            bool(status)
            str(login)
            str(senha)
        except ValueError as error:
            raise AssertionError("Campos obrigatório: login, senha")
        
        return UsuarioRepository.registerUsuario(Usuario(status, login, senha, cargo))
    
    def update(id, status, login, senha, cargo):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro")

        return UsuarioRepository.update(id, Usuario(status, login, senha, cargo)) 

    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro")

        assert int(id) > 0, "ID inválido"
        assert Usuario.query.filter(Usuario.id == id).first() is not None, "Usuario não encontrado" 
        return UsuarioRepository.delete(id)      
