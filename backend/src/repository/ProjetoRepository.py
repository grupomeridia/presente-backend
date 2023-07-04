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
    
    def update(id, data):
        projeto = Projeto.query.get(id)
        projeto.ativo = data['ativo']
        projeto.nome = data['nome']

        MainRepository.db.session.merge(projeto)
        MainRepository.db.session.commit()
        return {"mensagem":"sucesso"}
    
    def delete(id):
        projeto = Projeto.query.get(id)
        projeto.ativo = False

        MainRepository.db.session.merge(projeto)
        MainRepository.db.session.commit()

        return {"mensagem":"sucesso"}
    
    def register(projeto):

        MainRepository.db.session.add(projeto)
        MainRepository.db.session.commit()

        return f"Projeto cadastrado com o ID {projeto.id}"
