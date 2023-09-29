from flask import jsonify
from repository.MainRepository import MainRepository

from entity.Usuario import Usuario

class UsuarioRepository():
    def getUsuarioById(id):
        return{
            "id": Usuario.query.get(id).id_usuario,
            "Status": Usuario.query.get(id).status,
            "Login": Usuario.query.get(id).login,
            "Senha": Usuario.query.get(id).senha,
            "Cargo": Usuario.query.get(id).cargo.value
        }
    
    def register(usuario):
        MainRepository.db.session.add(usuario)
        MainRepository.db.session.commit()

        return "Usuario criado com sucesso"
    
    def update(id, data):
        usuario = Usuario.query.get(id)

        usuario.status = data.status
        usuario.login = data.login
        usuario.senha = data.senha
        usuario.cargo = data.cargo

        MainRepository.db.session.merge(usuario)
        MainRepository.db.session.commit()
        return {"mensagem":"sucesso"}
    
    def delete(id):
        usuario = Usuario.query.get(id)

        usuario.status = False

        MainRepository.db.session.merge(usuario)
        MainRepository.db.session.commit()

        return {"mensagem":"sucesso"}