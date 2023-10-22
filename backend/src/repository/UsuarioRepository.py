from flask_login import login_user
from models import db

from entity.Aluno import Aluno
from entity.Usuario import Usuario
from entity.Aluno import Aluno
from entity.Professor import Professor
from entity.Secretaria import Secretaria

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

        if (usuario.cargo.value == "Aluno"):
            aluno = Aluno(id_usuario=usuario.id_usuario, status=usuario.status, ausente=True, nome=usuario.nome, ra=usuario.ra)
            db.session.add(aluno)
            db.session.commit()

        if (usuario.cargo.value == "Professor"):
            professor = Professor(id_usuario=usuario.id_usuario, status=usuario.status, nome=usuario.nome)
            db.session.add(professor)
            db.session.commit()

        if (usuario.cargo.value == "Secretaria"):
            secretaria = Secretaria(id_usuario=usuario.id_usuario, status=usuario.status, nome=usuario.nome)
            db.session.add(secretaria)
            db.session.commit()

        return f"Usuario {usuario.id_usuario} criado com sucesso"
    
    @staticmethod
    def update(id, data):
        usuario = Usuario.query.get(id)

        usuario.status = data.status
        usuario.login = data.login
        usuario.senha = data.senha
        usuario.nome = data.nome
        usuario.cargo = data.cargo

        db.session.merge(usuario)
        db.session.commit()
        return f"Usuario {id} atualizado com sucesso"
    
    @staticmethod
    def delete(id):
        usuario = Usuario.query.get(id)

        usuario.status = False

        db.session.merge(usuario)
        db.session.commit()

        return f"Usuario {id} deletado com sucesso!"
    
    @staticmethod
    def login(login):
        user = Usuario.query.filter(Usuario.login == login).first()
        
        if login_user(user):
            return {
            "id_usuario":user.id_usuario,
            "Cargo": user.cargo.value,
            }
        else:
            raise AssertionError("Não foi possivel realizar o login!")
              

           