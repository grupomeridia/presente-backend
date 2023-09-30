from flask import jsonify
from models import db
from entity.Secretaria import Secretaria

class SecretariaRepository():
    @staticmethod
    def get_by_id(id):
        return {
            "Id": Secretaria.query.get(id).id,
            "Ativo": Secretaria.query.get(id).ativo,
            "Nome": Secretaria.query.get(id).nome,
            "Usuario": Secretaria.query.get(id).usuario.nome,
            "Lembrete": Secretaria.query.get(id).lembrete.mensagem
        }
    
    @staticmethod
    def list_all():
        secretaria = Secretaria.query.all()
        resultado = []
        for secre in secretaria:
            resultado.append({
                "Id": secre.id,
                "Ativo": secre.ativo,
                "Nome": secre.nome,
                "Usuario": secre.usuario.nome,
                "Lembrete": secre.lembrete.mensagem
            })
        
        return jsonify(resultado)
    
    @staticmethod
    def update(id, secretaria):
        old_secretaria = Secretaria.query.get(id)
        
        old_secretaria.idUsuario = secretaria.idUsuario
        old_secretaria.status = secretaria.status
        old_secretaria.nome = secretaria.nome
        
        db.session.merge(old_secretaria)
        db.session.commit()
        
        return f"Secretaria ID {id} atualizado."
    
    @staticmethod
    def delete(id):
        secretaria = Secretaria.query.get(id)
        secretaria.status = False
        db.session.merge(secretaria)
        db.session.commit()
        return f"Secretaria ID {id} deletado."
    
    @staticmethod
    def register_secretaria(secretaria):
        
        db.session.add(secretaria)
        db.session.commit()
        
        return f"Secretaria registrado com o ID {secretaria.id_secretaria}"