from flask import jsonify
from repository.MainRepository import MainRepository

from entity.Presenca import Presenca
from entity.Aluno import Aluno

class PresencaRepository():
    def getPresencaById(id):
        return {
            "Id" : Presenca.query.get(id).id,
            "Aluno": Presenca.query.get(id).idAluno.nome,
            "Chamada": Presenca.query.get(id).idChamada.id,
            "status": Presenca.query.get(id).status,
            "Tipo_presenca": Presenca.query.get(id).tipoPresenca.value,
            "Horario": Presenca.query.get(id).horario
        }
    
    def listAll():
        presencas = Presenca.query.all()
        resultado = [{
            "Id": p.id,
            "Aluno": p.idAluno.nome,
            "Chamada": p.idChamada,
            "status": p.status,
            "Tipo_presenca": p.tipoPresenca.value,
            "Horario": p.horario
        } for p in presencas]

        return jsonify(resultado)
    
    def findByPresentes():
        presencas = Presenca.query.filter(Presenca.horario.isnot(None)).all()

        resultado = [{
            "Id": p.id,
            "Aluno": p.idAluno.nome,
            "Chamada": p.idChamada,
            "status": p.status,
            "Tipo_presenca": p.tipoPresecna.value,
            "Horario": p.horario
        } for p in presencas]

        return jsonify(resultado)
    
    def update(id, data):
        presenca = Presenca.query.get(id)

        presenca.idAluno = data.idAluno
        presenca.idChamada = data.idChamada
        presenca.status = data.status
        presenca.tipoPresenca = data.tipoPresenca
        presenca.horario = data.horario

        MainRepository.db.session.merge(presenca)
        MainRepository.db.session.commit()

    def delete(id):
        presenca = Presenca.query.get(id)
        presenca.ativo = False
        MainRepository.db.session.merge(presenca)
        MainRepository.db.session.commit()

        return {"mensagem":"sucesso"}
    
    def registerPresenca(Presenca):

        MainRepository.db.session.add(Presenca)
        MainRepository.db.session.commit()

        return "Presença realizada!"