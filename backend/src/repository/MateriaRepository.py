from flask import jsonify
from repository.MainRepository import MainRepository

from entity.Materia import Materia

class MateriaRepository():
    def getMateriaById(id):
        return {
            "Id": Materia.query.get(id).id,
            "Ativo": Materia.query.get(id).ativo,
            "Nome": Materia.query.get(id).nome
        }
    
    def listAll():
        materia = Materia.query.all()
        resultado = [{
            "Id": p.id,
            "Nome": p.nome,
            "Ativo": p.ativo
        } for p in materia]

        return jsonify(resultado)
    
    def update(id, data):
        materia = Materia.query.get(id)
        materia.ativo = data.ativo
        materia.nome = data.nome

        MainRepository.db.session.merge(materia)
        MainRepository.db.session.commit()
        return {"mensagem":"sucesso"}
    
    def delete(id):
        materia = Materia.query.get(id)
        materia.ativo = False

        MainRepository.db.session.merge(materia)
        MainRepository.db.session.commit()

        return {"mensagem":"sucesso"}
    
    def register(materia):

        MainRepository.db.session.add(materia)
        MainRepository.db.session.commit()

        return f"Projeto cadastrado com o ID {materia.id_materia}"
