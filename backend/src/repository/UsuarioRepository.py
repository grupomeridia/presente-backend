from flask import jsonify
from models import db

from entity.Usuario import Usuario

class UsuarioRepository():
    @staticmethod
    def get_usuario_by_id(id):
        try:
            return{
                "id": Usuario.query.get(id).id_usuario,
                "Status": Usuario.query.get(id).status,
                "Login": Usuario.query.get(id).login,
                "Senha": Usuario.query.get(id).senha,
                "Cargo": Usuario.query.get(id).cargo.value
            }
        except AttributeError as error:
            raise AssertionError ("Usuário não existe.")
    
    @staticmethod
    def register(usuario):
        db.session.add(usuario)
        db.session.commit()

        return "Usuario criado com sucesso"
    
    @staticmethod
    def update(id, data):
        usuario = Usuario.query.get(id)

        usuario.status = data.status
        usuario.login = data.login
        usuario.senha = data.senha
        usuario.cargo = data.cargo

        db.session.merge(usuario)
        db.session.commit()
        return {"mensagem":"sucesso"}
    
    @staticmethod
    def delete(id):
        usuario = Usuario.query.get(id)

        usuario.status = False

        db.session.merge(usuario)
        db.session.commit()

        return {"mensagem":"sucesso"}