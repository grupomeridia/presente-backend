from flask import jsonify
from repository.MainRepository import MainRepository
import datetime

from entity.Chamada import Chamada
from entity.Presenca import Presenca
from entity.Turma import Turma
from entity.Aluno import Aluno
from entity.TurmaAluno import turma_aluno
from entity.Professor import Professor
from entity.Materia import Materia

class ChamadaRepository():
    def getChamadaById(id):
        return {
            "Id": Chamada.query.get(id).idChamada,
            "Materia" : Chamada.query.get(id).idMateria,
            "Turma" : Chamada.query.get(id).idTurma,
            "Professor" : Chamada.query.get(id).idProfessor,
            "status": Chamada.query.get(id).status,
            "abertura":Chamada.query.get(id).abertura,
            "encerramento": Chamada.query.get(id).encerramento
        }
    
    def listAll():
        chamadas = Chamada.query.filter(Chamada.ativo.isnot(False)).all()
        resultado = [{
            'Id': c.idChamada,
            'Materia': c.idMateria,
            'Turma': c.idTurma,
            'Professor': c.idProfessor,
            'status': c.status,
            'abertura': c.abertura,
            'encerramento': c.encerramento
        } for c in chamadas]

        return jsonify(resultado)
    
    def update(id, data):
        chamada = Chamada.query.get(id)

        chamada.idMateria = data['idMateria']
        chamada.idTurma = data['idTurma']
        chamada.idProfessor = data['idProfessor']
        chamada.status = data['status']
        chamada.abertura = data['abertura']
        chamada.encerramento = data['encerramento']

        MainRepository.db.session.merge(chamada)
        MainRepository.db.session.commit()
        return {"mensagem":"sucesso"}
    
    def delete(id):
        chamada = Chamada.query.get(id)

        if chamada:
            chamada.status = False
            MainRepository.db.session.merge(chamada)
            MainRepository.db.session.commit()
            return {"mensagem": "sucesso"}
        else:
            return {"mensagem": "Chamada não encontrada"}
    
    def registerChamada(Chamada):

        MainRepository.db.session.add(Chamada)
        MainRepository.db.session.commit()

        return "Chamada registrada"
    
    def getChamadasAbertasAluno(id):

        turma = MainRepository.db.session.query(Turma).join(turma_aluno).filter(Aluno.id == id).first()

        chamadas_abertas = MainRepository.db.session.query(Chamada, Turma, Professor, Materia).\
            filter(Chamada.turma == turma, Chamada.encerramento > datetime.now()).\
            join(Professor).\
            join(Materia).first()
        
        if chamadas_abertas:
                chamada, turma_curso, professor, materia = chamadas_abertas 
                return{
                    "Professor": professor.nome,
                    "Curso": turma_curso.curso,
                    "Materia": materia.nome,
                    "Data": chamada.abertura
                }
        else:
            return "Sem chamadas abertas no momento"

    def getHistoricoAluno(idAluno):
        
        ultimas_presencas = MainRepository.db.session.query(Presenca).\
        join(Chamada).\
        join(turma_aluno).\
        join(Turma).\
        filter(turma_aluno.c.idAluno == idAluno).\
        order_by(desc(Chamada.abertura)).\
        limit(5).all()

        resultado = [{
            "Data inicio": p.chamada.abertura,
            "Materia": p.chamada.materia.nome
        }for p in ultimas_presencas]

        return jsonify(resultado)

