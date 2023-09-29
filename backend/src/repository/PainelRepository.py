from flask import jsonify
from repository.MainRepository import MainRepository
import json

from entity.Painel import Painel

class PainelRepository():
    def getPainelById(id):
        return {
            "Id": Painel.query.get(id).id_secretaria,
            "Data": Painel.query.get(id).data_criado.strftime,
            "TotalAtivos": Painel.query.get(id).total_ativos,
            "TotalPresentes": Painel.query.get(id).total_presentes,
            "TotalAusentes": Painel.query.get(id).total_ausentes
        }
    
    def listAll():
        painel = Painel.query.all()
        resultado = [{
            "Id": p.id_secretaria,
            "Data": p.data_criado.strftime,
            "TotalAtivos": p.total_ativos,
            "TotalPresentes": p.total_presentes,
            "TotalAusentes": p.total_ausentes
        } for p in painel]

        return jsonify(resultado)
    
    def update(id, painel):
        old_painel = Painel.query.get(id)

        old_painel.data_criado = painel.data_criado
        old_painel.total_ativos = painel.total_ativos
        old_painel.total_presentes = painel.total_presentes
        old_painel.total_ausentes = painel.total_ausentes

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