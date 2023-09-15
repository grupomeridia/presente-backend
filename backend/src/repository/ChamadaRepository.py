from flask import jsonify
from repository.MainRepository import MainRepository

from entity.Chamada import Chamada



class ChamadaRepository():
    def getChamadaById(id):
        return {
            "Id": Chamada.query.get(id).idChamada,
            "Materia" : Chamada.query.get(id).idMateria,
            "Turma" : Chamada.query.get(id).idTurma,
            "Professor" : Chamada.query.get(id).idProfessor,
            "status": Chamada.query.get(id).status,
            "abertura":Chamada.query.get(id).abertura,
            "encerramento": Chamada.query.get(id).encerramento
        }
    
    def listAll():
        chamadas = Chamada.query.filter(Chamada.ativo.isnot(False)).all()
        resultado = [{
            'Id': c.idChamada,
            'Materia': c.idMateria,
            'Turma': c.idTurma,
            'Professor': c.idProfessor,
            'status': c.status,
            'abertura': c.abertura,
            'encerramento': c.encerramento
        } for c in chamadas]

        return jsonify(resultado)
    
    def update(id, data):
        chamada = Chamada.query.get(id)

        chamada.idMateria = data['idMateria']
        chamada.idTurma = data['idTurma']
        chamada.idProfessor = data['idProfessor']
        chamada.status = data['status']
        chamada.abertura = data['abertura']
        chamada.encerramento = data['encerramento']

        MainRepository.db.session.merge(chamada)
        MainRepository.db.session.commit()
        return {"mensagem":"sucesso"}
    
    def delete(id):
        chamada = Chamada.query.get(id)

        if chamada:
            chamada.status = False
            MainRepository.db.session.merge(chamada)
            MainRepository.db.session.commit()
            return {"mensagem": "sucesso"}
        else:
            return {"mensagem": "Chamada não encontrada"}
    
    def registerChamada(Chamada):

        MainRepository.db.session.add(Chamada)
        MainRepository.db.session.commit()

        return "Chamada registrada"