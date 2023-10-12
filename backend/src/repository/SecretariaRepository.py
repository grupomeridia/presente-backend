from flask import jsonify
from models import db
from entity.Secretaria import Secretaria

class SecretariaRepository():
    @staticmethod
    def get_by_id(id):
        try:
            return {
                "id": Secretaria.query.get(id).id_secretaria,
                "ativo": Secretaria.query.get(id).status,
                "nome": Secretaria.query.get(id).nome
            }
        except AttributeError as error:
            raise AssertionError ("Secretaria não existe.")
    @staticmethod
    def list_all():
        secretaria = Secretaria.query.all()
        resultado = []
        for secre in secretaria:
            resultado.append({
                "Id": secre.id,
                "Ativo": secre.ativo,
                "Nome": secre.nome,
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