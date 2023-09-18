from flask import jsonify
from repository.MainRepository import MainRepository

from entity.Usuario import Usuario

class UsuarioRepository():
    def getUsuarioById(id):
        return{
            "id": Usuario.query.get(id).idUsuario,
            "Status": Usuario.query.get(id).status,
            "Login": Usuario.query.get(id).login,
            "Senha": Usuario.query.get(id).senha,
            "Cargo": Usuario.query.get(id).cargo.value
        }
    
    def register(status, login, senha, cargo):
        MainRepository.db.session.add(Usuario(status, login, senha, cargo))
        MainRepository.db.session.commit()

        return "Usuario criado com sucesso"
    
    def update(id, status, login, senha, cargo):
        usuario = Usuario.query.get(id)

        usuario.status = status
        usuario.login = login
        usuario.senha = senha
        usuario.cargo = cargo

        MainRepository.db.session.merge(usuario)
        MainRepository.db.session.commit()
        return {"mensagem":"sucesso"}
    
    def delete(id):
        usuario = Usuario.query.get(id)

        usuario.ativo = False

        MainRepository.db.session.merge(usuario)
        MainRepository.db.session.commit()

        return {"mensagem":"sucesso"}