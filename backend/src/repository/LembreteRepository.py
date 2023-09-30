from flask import jsonify
from models import db
from entity.CargoEnum import Cargo
from entity.Lembrete import Lembrete

class LembreteRepository():
    @staticmethod
    def get_lembrete_by_id(id):
        return {
            "id_lembrete": Lembrete.query.get(id).id_lembrete,
            "id_secretaria" : Lembrete.query.get(id).id_secretaria,
            "DestinatarioId": Lembrete.query.get(id).destinatario_id,
            "DestinatarioCargo": Lembrete.query.get(id).destinatario_cargo,
            "Titulo": Lembrete.query.get(id).titulo,
            "Mensagem": Lembrete.query.get(id).mensagem,
            "Criacao": Lembrete.quey.get(id).criacao,
            "Visualizacao": Lembrete.query.get(id).visualizacao
        }
    
    @staticmethod
    def lista_all():
        lembretes = Lembrete.query.all()
        resultado = []
        for lembrete in lembretes:
            resultado.append({
                "id_lembrete" : lembrete.id_lembrete,
                "id_secretaria" : lembrete.id_secretaria, 
                "DestinatarioId": lembrete.destinatario_id,
                "DestinatarioCargo": lembrete.destinario_cargo,
                "Titulo": lembrete.titulo,
                "Mensagem": lembrete.mensagem,
                "Criacao": lembrete.criacao,
                "Visualizacao": lembrete.visualizacao
            })
        return jsonify(resultado)
    
    @staticmethod
    def update(id, lembrete):
        old_lembrete = Lembrete.query.get(id)
        
        old_lembrete.id_secretaria = lembrete.id_secretaria
        old_lembrete.destinatario_cargo = lembrete.destinatario_cargo
        old_lembrete.destinatario_id = lembrete.destinatario_id
        old_lembrete.titulo = lembrete.titulo
        old_lembrete.mensagem = lembrete.mensagem
        old_lembrete.criacao = lembrete.criacao
        old_lembrete.visualizacao = lembrete.visualizacao

        db.session.merge(old_lembrete)
        db.session.commit()
        
        return f"Lembrete ID {id} atualizado."
    
    @staticmethod
    def delete(id):
        lembrete = Lembrete.query.get(id)
        
        lembrete.status = False

        db.session.merge(lembrete)
        db.session.commit()
        
        return f"Lembrete ID {id} deletado."
    
    @staticmethod
    def create(lembrete):
        db.session.add(lembrete)
        db.session.commit()
        
        return f"Lembrete ID {lembrete.id_lembrete} criado."