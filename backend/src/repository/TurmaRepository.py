from flask import jsonify
from repository.MainRepository import MainRepository


from entity.Turma import Turma

class TurmaRepository():
    def getTurmaById(id):
        return {
               "Id":Turma.query.get(id).id,
               "Nome":Turma.query.get(id).nome,
               "Ativo": Turma.query.get(id).ativo,
               "Ano": Turma.query.get(id).ano,
               "Semestre": Turma.query.get(id).semestre}
    
    def listAll():
        turmas = Turma.query.all()
        resultado = [{
            "Id": t.id,
            "Nome": t.nome,
            "Ativo": t.ativo,
            "Ano": t.ano,
            "Semestre": t.semestre
        } for t in turmas]

        return jsonify(resultado)
    
    def update(id, data):
        turma = Turma.query.get(id)
        turma.nome = data['nome']
        turma.ativo = data['ativo']
        turma.ano = data['ano']
        turma.semestre = data['semestre']

        MainRepository.db.session.merge(turma)
        MainRepository.db.session.commit()
        return {"mensagem":"sucesso"}

    def delete(id):
        turma = Turma.query.get(id)
        turma.ativo = False

        MainRepository.db.session.merge(turma)
        MainRepository.db.session.commit()

        return {"mensagem":"sucesso"}
           