from flask import jsonify
from models import db
import json

from entity.Painel import Painel

class PainelRepository():
    @staticmethod
    def get_painel_by_id(id):
        try:
            return {
                "id_configuracao": Painel.query.get(id).id_configuracao,
                "id_secretaria": Painel.query.get(id).id_secretaria,
                "Data": Painel.query.get(id).data_criado,
                "TotalAtivos": Painel.query.get(id).total_ativo,
                "TotalPresentes": Painel.query.get(id).total_presentes,
                "TotalAusentes": Painel.query.get(id).total_ausentes
            }
        except AttributeError as error:
            raise AssertionError ("Painel não existe.")
    
    @staticmethod
    def list_all():
        painel = Painel.query.all()
        resultado = [{
            "Id": p.id_secretaria,
            "Data": p.data_criado,
            "TotalAtivos": p.total_ativos,
            "TotalPresentes": p.total_presentes,
            "TotalAusentes": p.total_ausentes
        } for p in painel]

        return jsonify(resultado)
    
    @staticmethod
    def update(id, painel):
        old_painel = Painel.query.get(id)

        old_painel.data_criado = painel.data_criado
        old_painel.total_ativos = painel.total_ativos
        old_painel.total_presentes = painel.total_presentes
        old_painel.total_ausentes = painel.total_ausentes

        db.session.merge(old_painel)
        db.session.commit()

        return f"Painel ID {id} atualizado."
    
    @staticmethod
    def delete(id):
        painel = Painel.query.get(id)

        painel.status = False

        db.session.merge(painel)
        db.session.commit()
        return f"Painel ID {id} deletado."

    @staticmethod
    def register_painel(painel):
        db.session.add(painel)
        db.session.commit()
        return f"Painel registrado com o ID {painel.id_painel}"