from flask import jsonify
from repository.MainRepository import MainRepository


from entity.Turma import Turma

class TurmaRepository():
    def getTurmaById(id):
        return {
               "Id":Turma.query.get(id).idTurma,
               "status":Turma.query.get(id).status,
               "nome": Turma.query.get(id).nome,
               "Ano": Turma.query.get(id).ano,
               "Semestre": Turma.query.get(id).semestre,
               "turno": Turma.query.get(id).turno,
               "modalidade": Turma.query.get(id).modalidade,
               "curso": Turma.query.get(id).curso
               } 
    
    def listAll():
        turmas = Turma.query.all()
        resultado = [{
            "Id": t.id,
            "status": t.status,
            "Nome": t.nome,
            "Ano": t.ano,
            "Semestre": t.semestre,
            "turno": t.turno,
            "modalidade": t.modalidade,
            "curso": t.curso
        } for t in turmas]

        return jsonify(resultado)
    
    def update(id, data):
        turma = Turma.query.get(id)

        turma.nome = data['nome']
        turma.ano = data['ano']
        turma.semestre = data['semestre']
        turma.turno = data['turno']
        turma.modalidade = data['modalidade']
        turma.curso = data['curso']

        MainRepository.db.session.merge(turma)
        MainRepository.db.session.commit()
        return {"mensagem":"sucesso"}

    def delete(id):
        turma = Turma.query.get(id)
        turma.ativo = False

        MainRepository.db.session.merge(turma)
        MainRepository.db.session.commit()

        return {"mensagem":"sucesso"}
           
    def register(turma):
        
        MainRepository.db.session.add(turma)
        MainRepository.db.session.commit()

        return f"Turma Cadastrada com o ID {turma.id}!"