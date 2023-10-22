from flask import jsonify
from models import db

from datetime import datetime

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
                "id_chamada": Chamada.query.get(id).id_chamada,
                "turma" : Chamada.query.get(id).id_turma,
                "professor" : Chamada.query.get(id).id_professor,
                "status": Chamada.query.get(id).status,
                "abertura":Chamada.query.get(id).abertura,
                "encerramento": Chamada.query.get(id).encerramento
            }
        except AttributeError as error:
            raise AssertionError ("Chamada não existe.")
    
    @staticmethod
    def listar_all_chamadas_professor(id_professor):
        consulta_sql = db.text("""
        SELECT * FROM chamadas WHERE id_professor = :id_professor and encerramento IS NULL

    """)
        
        with db.engine.connect() as connection:
            resultado = connection.execute(consulta_sql, {'id_professor': id_professor}).fetchall()
        
        resultado_json = []
        for id_chamada, id_turma, id_professor, status, abertura, encerramento in resultado:
            professor_nome = Professor.query.get(id_professor)
            turma_nome = Turma.query.get(id_turma)
            resultado_json.append({
                'id_chamada': id_chamada,
                'id_professor': professor_nome.nome,
                'id_turma': turma_nome.nome,
                'status': status,
                'abertura': abertura,
                'encerramento': encerramento
            })

        return resultado_json

    @staticmethod
    def list_all():
        chamadas = Chamada.query.filter(Chamada.status.isnot(False)).all()
        resultado = [{
            'Id': c.id_chamada,
            'Turma': c.id_turma,
            'Professor': c.id_professor,
            'status': c.status,
            'abertura': c.abertura,
            'encerramento': c.encerramento
        } for c in chamadas]

        return jsonify(resultado)
    
    @staticmethod
    def update(id, data):
        print("AQUI CARAIOOO",id)
        chamada = Chamada.query.get(id)
        
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
    def fechar_chamada(id_chamada):
        chamada = Chamada.query.get(id_chamada)

        if chamada:
            chamada.encerramento = datetime.now()
            db.session.merge(chamada)
            db.session.commit()
            return {"mensagem": "Chamada fechada com sucesso"}
        else:
            return {"mensagem": "Chamada não encontrada"}

    @staticmethod
    def register_chamada(chamada):

        db.session.add(chamada)
        db.session.commit()

        return "Chamada registrada"
    
    @staticmethod
    def get_chamadas_abertas_aluno(id):

        consulta_sql = db.text("""
        select c.* from chamadas c 
        join turma_aluno ta on ta.id_turma = c.id_turma
        where ta.id_aluno = :id and encerramento IS NULL
    
    """)
        
        with db.engine.connect() as connection:    
            resultado = connection.execute(consulta_sql, {'id': id}).fetchall()
            
        resultado_json = []
        for id_chamada, id_turma, id_professor, status, abertura, encerramento in resultado:
            resultado_json.append({
                'id_chamada': id_chamada,
                'id_professor': id_professor,
                'id_turma': id_turma,
                'status': status,
                'abertura': abertura,
                'encerramento': encerramento
            })

        return resultado_json

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

