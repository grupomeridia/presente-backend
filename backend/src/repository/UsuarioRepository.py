from flask_login import login_user
from flask_jwt_extended import create_access_token, jwt_required

from models import db

from entity.Aluno import Aluno
from entity.Usuario import Usuario
from entity.Aluno import Aluno
from entity.Professor import Professor
from entity.Secretaria import Secretaria
from entity.Turma import Turma

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
            aluno = Aluno(id_usuario=usuario.id_usuario, status=usuario.status, ausente=False, nome=usuario.nome, ra=usuario.ra)
            db.session.add(aluno)
            db.session.commit()

            return {"id_aluno": aluno.id_aluno}

        if (usuario.cargo.value == "Professor"):
            professor = Professor(id_usuario=usuario.id_usuario, status=usuario.status, nome=usuario.nome)
            db.session.add(professor)
            db.session.commit()

            return {"id_professor": professor.id_professor}

        if (usuario.cargo.value == "Secretaria"):
            secretaria = Secretaria(id_usuario=usuario.id_usuario, status=usuario.status, nome=usuario.nome)
            db.session.add(secretaria)
            db.session.commit()

            return {"id_secretaria": secretaria.id_secretaria}

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
            access_token = create_access_token(identity=user.login)
            if user.cargo.value == "Aluno":  
                aluno = Aluno.query.filter(Aluno.id_usuario == user.id_usuario).first()  

                consulta_sql = db.text("""SELECT t.curso FROM turma_aluno ta
                    JOIN alunos a ON a.id_aluno = ta.id_aluno
                    JOIN turmas t ON t.id_turma = ta.id_turma """)

                with db.engine.connect() as connection:
                    curso = connection.execute(consulta_sql).fetchone()

                return {
                "id_usuario":user.id_usuario,
                "id_aluno":aluno.id_aluno,
                "Curso": curso.curso,
                "Cargo": user.cargo.value,
                "Nome": user.nome,
                "RA":aluno.ra,
                "JWT":access_token
                }
            
            elif user.cargo.value == "Professor":
                professor = Professor.query.filter(Professor.id_usuario == user.id_usuario).first()
                return{
                    "id_usuario":user.id_usuario,
                    "id_professor":professor.id_professor,
                    "Cargo": user.cargo.value,
                    "Nome": user.nome,
                    "JWT":access_token
                }
            
            elif user.cargo.value == "Secretaria":
                secretaria = Secretaria.query.filter(Secretaria.id_usuario == user.id_usuario).first()
                return{
                    "id_usuario":user.id_usuario,
                    "id_secretaria":secretaria.id_secretaria,
                    "Cargo": user.cargo.value,
                    "Nome": user.nome,
                    "JWT":access_token
                }
        else:
            raise AssertionError("Não foi possivel realizar o login!")
              

           