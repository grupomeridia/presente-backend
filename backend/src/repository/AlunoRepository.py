from flask import jsonify
from repository.MainRepository import MainRepository
import json

from entity.Aluno import Aluno

class AlunoRepository():
    def getAlunoById(id):
        return {
            "id": Aluno.query.get(id).id_aluno,
            "id_usuario" : Aluno.query.get(id).id_usuario,
            "Nome": Aluno.query.get(id).nome,
            "RA": Aluno.query.get(id).ra,
            "Ativo": Aluno.query.get(id).status,
            "Ausente": Aluno.query.get(id).ausente
        }

    def listAll():
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
    
    def update(id, aluno):
        old_aluno = Aluno.query.get(id)

        old_aluno.status = aluno.status
        old_aluno.nome = aluno.nome
        old_aluno.ra = aluno.ra
        old_aluno.ausente = aluno.ausente

        MainRepository.db.session.merge(old_aluno)
        MainRepository.db.session.commit()

        return f"Aluno ID {id} atualizado"
        
    def delete(id):
        aluno = Aluno.query.get(id)
        aluno.ativo = False
        MainRepository.db.session.merge(aluno)
        MainRepository.db.session.commit()
        return f"Aluno ID {id} deletado"
    
    def findByRA(ra):
        aluno = Aluno.query.filter(Aluno.ra == ra).first()
        return {
            "Id": aluno.id_aluno,
            "id_usuario" : aluno.id_usuario,
            "Nome": aluno.nome,
            "RA": aluno.ra,
            "Ativo": aluno.status,
            "Ausente" : aluno.ausente
        }
        
    def registerAluno(Aluno):

        MainRepository.db.session.add(Aluno)
        MainRepository.db.session.commit()

        return f"Aluno registrado com o ID {Aluno.id_aluno}"
    
   
