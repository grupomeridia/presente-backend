from flask import jsonify
from repository.MainRepository import MainRepository

from entity.Presenca import Presenca
from entity.Aluno import Aluno

class PresencaRepository():
    def getPresencaById(id):
        return {
            "Id" : Presenca.query.get(id).id,
            "Aluno_ra": Presenca.query.get(id).aluno.ra,
            "Turma": Presenca.query.get(id).turma.nome,
            "Projeto": Presenca.query.get(id).projeto.nome,
            "Chamada": Presenca.query.get(id).chamada_id,
            "Professor": Presenca.query.get(id).professor.nome,
            "Tipo_presenca": Presenca.query.get(id).tipo_presenca.value,
            "Horario": Presenca.query.get(id).horario

        }
    
    def listAll():
        presencas = Presenca.query.all()
        resultado = [{
            "Id": p.id,
            "Aluno_ra": p.aluno.ra,
            "Turma": p.turma.nome,
            "Projeto": p.projeto.nome,
            "Chamada": p.chamada_id,
            "Professor": p.professor.nome,
            "Tipo_presenca": p.tipo_presenca.value,
            "Horario": p.horario
        } for p in presencas]

        return jsonify(resultado)
    
    def findByPresentes():
        presencas = Presenca.query.filter(Presenca.horario.isnot(None)).all()

        resultado = [{
            "Id": p.id,
            "Aluno_ra": p.aluno_ra,
            "Aluno_nome": p.aluno.nome,
            "Turma": p.turma.nome,
            "Projeto": p.projeto.nome,
            "Chamada": p.chamada_id,
            "Professor": p.professor.nome,
            "Tipo_presenca": p.tipo_presenca.value,
            "Horario": p.horario
        } for p in presencas]

        return jsonify(resultado)
    
    def update(id, data):
        presenca = Presenca.query.get(id)

        presenca.ativo = data['ativo']
        presenca.aluno_ra = data['AlunoRa']
        presenca.turma = data['turma']
        presenca.projeto = data['projeto']
        presenca.chamada = data['chamada']
        presenca.professor = data['professor']
        presenca.tipo_presenca = data['tipoPresenca']
        presenca.horario = data['horario']

        MainRepository.db.session.merge(presenca)
        MainRepository.db.session.commit()

    def delete(id):
        presenca = Presenca.query.get(id)
        presenca.ativo = False
        MainRepository.db.session.merge(presenca)
        MainRepository.db.session.commit()

        return {"mensagem":"sucesso"}
    
    def registerPresenca(Presenca):

        MainRepository.db.session.add(Presenca)
        MainRepository.db.session.commit()

        return "Presença realizada!"