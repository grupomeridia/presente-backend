from flask import jsonify
from repository.MainRepository import MainRepository
import json

from entity.Painel import Painel

class PainelRepository():
    def getPainelById(id):
        return {
            "Id": Painel.query.get(id).id,
            "Data": Painel.query.get(id).data.strftime,
            "TotalAtivos": Painel.query.get(id).totalAtivos,
            "TotalPresentes": Painel.query.get(id).totalPresentes,
            "TotalAusentes": Painel.query.get(id).totalAusentes,
            "TotalPresentesCurso": Painel.query.get(id).totalPresentesCurso,
            "TotalAtivoCurso": Painel.query.get(id).totalAtivoCurso,
            "TotalAusenteCurso": Painel.query.get(id).totalAusenteCurso
        }
    
    def listAll():
        painel = Painel.query.all()
        resultado = [{
            "Id": p.id,
            "Data": p.data.strftime,
            "TotalAtivos": p.totalAtivos,
            "TotalPresentes": p.totalPresentes,
            "TotalAusentes": p.totalAusentes,
            "TotalPresentesCurso": p.totalPresentesCurso,
            "TotalAtivoCurso": p.totalAtivoCurso,
            "TotalAusenteCurso": p.totalAusenteCurso
        } for p in painel]

        return jsonify(resultado)
    
    def update(id, painel):
        old_painel = Painel.query.get(id)

        old_painel.data = painel.data
        old_painel.totalAtivos = painel.totalAtivos
        old_painel.totalPresentes = painel.totalPresentes
        old_painel.totalAusentes = painel.totalAusentes
        old_painel.totalPresentesCurso = painel.totalPresentesCurso
        old_painel.totalAtivoCurso = painel.totalAtivoCurso
        old_painel.totalAusenteCurso = painel.totalAusenteCurso

        MainRepository.db.session.merge(old_painel)
        MainRepository.db.session.commit()

        return f"Painel ID {id} atualizado."
    
    def delete(id):
        painel = Painel.query.get(id)
        MainRepository.db.session.delete(painel)
        MainRepository.db.session.commit()
        return f"Painel ID {id} deletado."

    def registerPainel(painel):
        MainRepository.db.session.add(painel)
        MainRepository.db.session.commit()
        return f"Painel registrado com o ID {painel.id_painel}"