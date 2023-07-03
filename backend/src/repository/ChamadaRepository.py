from flask import jsonify
from repository.MainRepository import MainRepository

from entity.Chamada import Chamada



class ChamadaRepository():
    def getChamadaById(id):
        return {
            "Id": Chamada.query.get(id).id,
            "Ativo" : Chamada.query.get(id).ativo,
            "Projeto" : Chamada.query.get(id).projeto_id,
            "Professor" : Chamada.query.get(id).professor_id,
            "Turma": Chamada.query.get(id).turma_id
        }
    
    def listAll():
        chamadas = Chamada.query.filter(Chamada.ativo.isnot(False)).all()
        resultado = [{
            'Id': c.id,
            'Ativo': c.ativo,
            'Projeto': c.projeto.nome,
            'Professor': c.professor.nome,
            'turma': c.turma.nome
        } for c in chamadas]
        
        return jsonify(resultado)
    
    def update(i, data):
        chamada = Chamada.query.get(id)
        chamada.ativo = data['ativo']
        chamada.projeto_id = data['projeto']
        chamada.professor_id = data['professor']
        chamada.turma_id = data['turma']

        MainRepository.db.session.merge(chamada)
        MainRepository.db.session.commit()
        return {"mensagem":"suecesso"}
    
    def delete(id):
        chamada = Chamada.query.get(id)
        chamada.ativo = False

        MainRepository.db.session.merge(chamada)
        MainRepository.db.session.commit()

        return {"mensagem":"sucesso"}