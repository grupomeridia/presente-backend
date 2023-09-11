from flask import jsonify
from repository.MainRepository import MainRepository

from entity.Secretaria import Secretaria

class SecretariaRepository():
    def getById(id):
        return {
            "Id": Secretaria.query.get(id).id,
            "Ativo": Secretaria.query.get(id).ativo,
            "Nome": Secretaria.query.get(id).nome,
            "Usuario": Secretaria.query.get(id).usuario.nome,
            "Lembrete": Secretaria.query.get(id).lembrete.mensagem
        }
    
    def listAll():
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
    
    def update(id, secretaria):
        old_secretaria = Secretaria.query.get(id)
        
        old_secretaria.ativo = secretaria.ativo
        old_secretaria.nome = secretaria.nome
        old_secretaria.usuario = secretaria.usuario
        old_secretaria.lembrete = secretaria.lembrete
        
        MainRepository.db.session.merge(old_secretaria)
        MainRepository.db.session.commit()
        
        return f"Secretaria ID {id} atualizado."
    
    def delete(id):
        secretaria = Secretaria.query.get(id)
        secretaria.ativo = False
        MainRepository.db.session.merge(secretaria)
        MainRepository.db.session.commit()
        return f"Secretaria ID {id} deletado."
    
    def registerSecretaria(Secretaria):
        
        MainRepository.db.session.add(Secretaria)
        MainRepository.db.session.commit()
        
        return f"Usuario registrado com o ID {Secretaria.id}"