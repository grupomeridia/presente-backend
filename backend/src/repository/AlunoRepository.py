from flask import jsonify
from repository.MainRepository import MainRepository
import json

from entity.Aluno import Aluno

class AlunoRepository():
    def getAlunoById(id):
        return {
            "Id": Aluno.query.get(id).id,
            "Nome": Aluno.query.get(id).nome,
            "RA": Aluno.query.get(id).ra,
            "Ativo": Aluno.query.get(id).ativo,
            "Turma": Aluno.query.get(id).turma.nome,
            "Curso": Aluno.query.get(id).curso.value
        }

    def listAll():
        alunos = Aluno.query.all()
        resultado = [{
            "Id": a.id,
            "Nome": a.nome,
            "RA": a.ra,
            "Ativo": a.ativo,
            "Turma": a.turma.nome,
            "Curso": a.curso.value
        } for a in alunos]

        return jsonify(resultado)
    
    def update(id, aluno):
        old_aluno = Aluno.query.get(id)

        old_aluno.ativo = aluno.ativo
        old_aluno.nome = aluno.nome
        old_aluno.ra = aluno.ra
        old_aluno.turma_id = aluno.turma_id
        old_aluno.curso = aluno.curso

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
            "Id": aluno.id,
            "Nome": aluno.nome,
            "RA": aluno.ra,
            "Ativo": aluno.ativo,
            "Turma": aluno.turma.nome,
            "Curso": aluno.curso.value
        }
        
    def registerAluno(Aluno):

        MainRepository.db.session.add(Aluno)
        MainRepository.db.session.commit()

        return f"Aluno registrado com o ID {Aluno.id}"
    
   
