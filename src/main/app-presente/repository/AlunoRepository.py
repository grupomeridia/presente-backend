from flask import jsonify
from repository.MainRepository import MainRepository

from entity.Aluno import Aluno

class AlunoRepository():
    def getAlunoById(id):
        return {
            "Id": Aluno.query.get(id).id,
            "Nome": Aluno.query.get(id).nome,
            "RA": Aluno.query.get(id).ra,
            "Ativo": Aluno.query.get(id).ativo,
            "Turma": Aluno.query.get(id).turma_id,
            "Curso": Aluno.query.get(id).curso.value
        }
    
    def listAll():
        alunos = Aluno.query.all()
        resultado = [{
            "Id": a.id,
            "Nome": a.nome,
            "RA": a.ra,
            "Ativo": a.ativo,
            "Turma": a.turma_id,
            "Curso": a.curso.value
        } for a in alunos]

        return jsonify(resultado)