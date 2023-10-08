from flask import jsonify
from models import db

import datetime

from entity.Chamada import Chamada
from entity.Presenca import Presenca
from entity.Turma import Turma
from entity.Aluno import Aluno
from entity.TurmaAluno import turma_aluno
from entity.Professor import Professor
from entity.Materia import Materia

class ChamadaRepository():
    @staticmethod
    def get_chamada_by_id(id):
        try:
            return {
                "Id": Chamada.query.get(id).id_chamada,
                "Materia" : Chamada.query.get(id).id_materia,
                "Turma" : Chamada.query.get(id).id_turma,
                "Professor" : Chamada.query.get(id).id_professor,
                "status": Chamada.query.get(id).status,
                "abertura":Chamada.query.get(id).abertura,
                "encerramento": Chamada.query.get(id).encerramento
            }
        except AttributeError as error:
            raise AssertionError ("Chamada não existe.")
    @staticmethod
    def list_all():
        chamadas = Chamada.query.filter(Chamada.ativo.isnot(False)).all()
        resultado = [{
            'Id': c.id_chamada,
            'Materia': c.id_materia,
            'Turma': c.id_turma,
            'Professor': c.id_professor,
            'status': c.status,
            'abertura': c.abertura,
            'encerramento': c.encerramento
        } for c in chamadas]

        return jsonify(resultado)
    
    @staticmethod
    def update(id, data):
        chamada = Chamada.query.get(id)

        chamada.id_materia = data.id_materia
        chamada.id_turma = data.id_turma
        chamada.id_professor = data.id_professor
        chamada.status = data.status
        chamada.abertura = data.abertura
        chamada.encerramento = data.encerramento

        db.session.merge(chamada)
        db.session.commit()
        return {"mensagem":"sucesso"}
    
    @staticmethod
    def delete(id):
        chamada = Chamada.query.get(id)

        if chamada:
            chamada.status = False
            db.session.merge(chamada)
            db.session.commit()
            return {"mensagem": "sucesso"}
        else:
            return {"mensagem": "Chamada não encontrada"}
    
    @staticmethod
    def register_chamada(chamada):

        db.session.add(chamada)
        db.session.commit()

        return "Chamada registrada"
    
    @staticmethod
    def get_chamadas_abertas_aluno(id):

        turma = db.session.query(Turma).join(turma_aluno).filter(Aluno.id_aluno == id).first()

        chamadas_abertas = db.session.query(Chamada, Turma, Professor, Materia).\
            filter(Chamada.id_turma == turma, Chamada.encerramento > datetime.now()).\
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

    @staticmethod
    def get_historico_aluno(id_aluno):
        
        ultimas_presencas = db.session.query(Presenca).\
        join(Chamada).\
        join(turma_aluno).\
        join(Turma).\
        filter(turma_aluno.c.id_aluno == id_aluno).\
        order_by(db.desc(Chamada.abertura)).\
        limit(5).all()

        resultado = [{
            "Data inicio": p.chamada.abertura,
            "Materia": p.chamada.materia.nome
        }for p in ultimas_presencas]

        return jsonify(resultado)

