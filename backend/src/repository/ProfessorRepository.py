from flask import jsonify
from repository.MainRepository import MainRepository

from entity.Professor import Professor

class ProfessorRepository():
    def getProfessorById(id):
        return {
            "Id": Professor.query.get(id).id,
            "Nome": Professor.query.get(id).nome,
            "Ativo": Professor.query.get(id).ativo
        }
    
    def listAll():
        professores = Professor.query.all()
        resultado = [{
            'Id': p.id, 
            'Nome': p.nome, 
            'Ativo': p.ativo
        } for p in professores]

        return jsonify(resultado)
    
    def update(id, data):
        professor = Professor.query.get(id)
        professor.nome = data['nome']
        professor.ativo = data['ativo']


        MainRepository.db.session.merge(professor)
        MainRepository.db.session.commit()
        return {"mensagem":"sucesso"}
  
    def delete(id):
        professor = Professor.query.get(id)
        professor.ativo = False
        
        MainRepository.db.session.merge(professor)
        MainRepository.db.session.commit()


        return {"mensagem":"sucesso"}