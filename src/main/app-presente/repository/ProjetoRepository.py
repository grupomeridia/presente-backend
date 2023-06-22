from flask import jsonify
from repository.MainRepository import MainRepository

from entity.Projeto import Projeto

class ProjetoRepository():
    def getProjetoById(id):
        return {
            "Id": Projeto.query.get(id).id,
            "Ativo": Projeto.query.get(id).ativo,
            "Nome": Projeto.query.get(id).nome
        }
    
    def listAll():
        projetos = Projeto.query.all()
        resultado = [{
            "Id": p.id,
            "Nome": p.nome,
            "Ativo": p.ativo
        } for p in projetos]

        return jsonify(resultado)