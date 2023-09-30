from flask import jsonify
from models import db
from entity.Aluno import Aluno

class AlunoRepository():
    @staticmethod
    def get_aluno_by_id(id):
        return {
            "id": Aluno.query.get(id).id_aluno,
            "id_usuario" : Aluno.query.get(id).id_usuario,
            "Nome": Aluno.query.get(id).nome,
            "RA": Aluno.query.get(id).ra,
            "Ativo": Aluno.query.get(id).status,
            "Ausente": Aluno.query.get(id).ausente
        }
    
    @staticmethod
    def list_all():
        alunos = Aluno.query.all()
        resultado = [{
            "id": a.id_aluno,
            "id_usuario" : a.id_usuario,
            "Nome": a.nome,
            "RA": a.ra,
            "Ativo": a.status,
            "Ausente" : a.ausente
        } for a in alunos]

        return jsonify(resultado)
    
    @staticmethod
    def update(id, aluno):
        old_aluno = Aluno.query.get(id)

        old_aluno.status = aluno.status
        old_aluno.nome = aluno.nome
        old_aluno.ra = aluno.ra
        old_aluno.ausente = aluno.ausente

        db.session.merge(old_aluno)
        db.session.commit()

        return f"Aluno ID {id} atualizado"
    
    @staticmethod
    def delete(id):
        aluno = Aluno.query.get(id)
        aluno.status = False
        db.session.merge(aluno)
        db.session.commit()
        return f"Aluno ID {id} deletado"
    
    @staticmethod
    def find_by_ra(ra):
        aluno = Aluno.query.filter(Aluno.ra == ra).first()
        return {
            "Id": aluno.id_aluno,
            "id_usuario" : aluno.id_usuario,
            "Nome": aluno.nome,
            "RA": aluno.ra,
            "Ativo": aluno.status,
            "Ausente" : aluno.ausente
        }
        
    @staticmethod
    def register_aluno(aluno):

        db.session.add(aluno)
        db.session.commit()

        return f"Aluno registrado com o ID {aluno.id_aluno}"
    
   
