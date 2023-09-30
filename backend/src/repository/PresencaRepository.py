from flask import jsonify
from models import db

from entity.Presenca import Presenca
from entity.Aluno import Aluno

class PresencaRepository():
    @staticmethod
    def get_presenca_by_id(id):
        return {
            "Id" : Presenca.query.get(id).id,
            "Aluno": Presenca.query.get(id).idAluno.nome,
            "Chamada": Presenca.query.get(id).idChamada.id,
            "status": Presenca.query.get(id).status,
            "Tipo_presenca": Presenca.query.get(id).tipoPresenca.value,
            "Horario": Presenca.query.get(id).horario
        }
    
    @staticmethod
    def list_all():
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
    
    @staticmethod
    def find_by_presentes():
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
    
    @staticmethod
    def update(id, data):
        presenca = Presenca.query.get(id)

        presenca.idAluno = data.idAluno
        presenca.idChamada = data.idChamada
        presenca.status = data.status
        presenca.tipoPresenca = data.tipoPresenca
        presenca.horario = data.horario

        db.session.merge(presenca)
        db.session.commit()

    @staticmethod
    def delete(id):
        presenca = Presenca.query.get(id)
        presenca.ativo = False
        db.session.merge(presenca)
        db.session.commit()

        return {"mensagem":"sucesso"}
    
    @staticmethod
    def register_presenca(presenca):

        db.session.add(presenca)
        db.session.commit()

        return "Presença realizada!"