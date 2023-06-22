from flask import jsonify
from repository.MainRepository import MainRepository

from entity.Presenca import Presenca

class PresencaRepository():
    def getAlunoById(id):
        return {
            "Id" : Presenca.query.get(id).id,
            "Aluno_ra": Presenca.query.get(id).aluno_ra,
            "Turma": Presenca.query.get(id).turma_id,
            "Projeto": Presenca.query.get(id).projeto_id,
            "Chamada": Presenca.query.get(id).chamada_id,
            "Professor": Presenca.query.get(id).professor_id,
            "Tipo_presenca": Presenca.query.get(id).tipo_presenca.value,
            "Horario": Presenca.query.get(id).horario

        }
    
    def listAll():
        presencas = Presenca.query.all()
        resultado = [{
            "Id": p.id,
            "Aluno_ra": p.aluno_ra,
            "Turma": p.turma_id,
            "Projeto": p.projeto_id,
            "Chamada": p.chamada_id,
            "Professor": p.professor_id,
            "Tipo_presenca": p.tipo_presenca.value,
            "Horario": p.horario
        } for p in presencas]

        return jsonify(resultado)
    
    def findByPresentes():
        presencas = Presenca.query.filter(Presenca.horario.isnot(None)).all()
        resultado = [{
            "Id": p.id,
            "Aluno_ra": p.aluno_ra,
            "Turma": p.turma_id,
            "Projeto": p.projeto_id,
            "Chamada": p.chamada_id,
            "Professor": p.professor_id,
            "Tipo_presenca": p.tipo_presenca.value,
            "Horario": p.horario
        } for p in presencas]

        return jsonify(resultado)