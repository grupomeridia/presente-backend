from flask import jsonify
from models import db
from threading import Timer

from datetime import datetime

from entity.Chamada import Chamada
from entity.Presenca import Presenca
from entity.Turma import Turma
from entity.Aluno import Aluno
from entity.TurmaAluno import turma_aluno
from entity.Professor import Professor
from entity.Configuracao import Configuracao

from sqlalchemy import select

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
            SELECT c.*, m.nome FROM chamadas c 
            JOIN turmas t ON t.id_turma = c.id_turma
            JOIN materias m ON m.id_materia = t.id_materia
            WHERE c.id_professor = :id_professor and c.status is True

    """)
        
        with db.engine.connect() as connection:
            resultado = connection.execute(consulta_sql, {'id_professor': id_professor}).fetchall()
        
        resultado_json = []
        for id_chamada, id_turma, id_professor, status, abertura, encerramento, nome_materia in resultado:
            professor_nome = Professor.query.get(id_professor)
            turma_nome = Turma.query.get(id_turma)
            resultado_json.append({
                'id_chamada': id_chamada,
                'id_professor': professor_nome.nome,
                'id_turma': turma_nome.nome,
                'id_novo': turma_nome.id_turma,
                'status': status,
                'abertura': abertura,
                'encerramento': encerramento,
                'nome_materia': nome_materia
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
            if (chamada.encerramento == None):
                chamada.encerramento = datetime.now()

            chamada.status = False
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
            select p.nome, m.nome, c.id_chamada, c.abertura, c.encerramento from chamadas c 
            join turma_aluno ta on ta.id_turma = c.id_turma
            join professores p on p.id_professor = c.id_professor
            join turmas t on t.id_turma = ta.id_turma
            join materias m on m.id_materia = t.id_materia
            where ta.id_aluno = :id and c.status is True 
            and (ta.id_aluno, c.id_chamada) NOT IN (
                SELECT id_aluno, id_chamada FROM presencas)
            """)
        
        with db.engine.connect() as connection:    
            resultado = connection.execute(consulta_sql, {'id': id}).fetchall()
            
        resultado_json = []
        for professor_nome, materia_nome, id_chamada, abertura, encerramento in resultado:
            resultado_json.append({
                'professor_nome': professor_nome,
                'materia_nome': materia_nome,
                'id_chamada': id_chamada,
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

    @staticmethod
    def update_all():
        with db.engine.connect() as connection:    
            chamadas = connection.execute(select(Chamada).where(Chamada.status == True)).all()
            config = Configuracao.query.filter(Configuracao.status == True).first()
            
            for x in range(len(chamadas)):
                if chamadas[x].encerramento < datetime.now() or (config is not None and chamadas[x].encerramento < config.fim_aula):
                    chamada = Chamada.query.get(chamadas[x].id_chamada)
                    chamada.status = False
                    db.session.merge(chamada)
                    db.session.commit()

        return "Chamadas atualizadas"
    
    @staticmethod
    def ultimaChamada(id_professor):
        consulta_sql = db.text("""
        SELECT c.* FROM chamadas c
        WHERE c.id_professor = :id_professor
        AND c.status = false
        AND c.encerramento IS NOT NULL
        ORDER BY c.encerramento DESC
        LIMIT 1
        """)

        with db.engine.connect() as connection:
            chamada = connection.execute(consulta_sql, {'id_professor':id_professor}).fetchone()

            id_chamada = chamada[0]
            id_turma = chamada[1]
            id_professor = chamada[2]
            status = chamada[3]
            abertura = chamada[4]
            encerramento = chamada[5]

            ultima_chamada = {
                'id_chamada': id_chamada,
                'id_turma': id_turma,
                'id_professor': id_professor,
                'status': status,
                'abertura': abertura,
                'encerramento': encerramento
            }

            return ultima_chamada
        
    @staticmethod
    def marcarFaltas(id_turma, id_chamada):
        alunos = db.session.query(Aluno).join(turma_aluno).join(Turma).filter(Turma.id_turma == id_turma).all()        

        for aluno in alunos:
            presencas = db.session.query(Presenca).filter((Presenca.id_aluno == aluno.id_aluno) & (Presenca.id_chamada == id_chamada)).first()
            if presencas is None:
                presenca = Presenca(
                    id_aluno=aluno.id_aluno,
                    id_chamada=id_chamada,
                    status=False,
                    horario=None,
                    tipo_presenca="Regular"
                )
                db.session.add(presenca)
                db.session.commit()


        return "Sucesso!"
            
    
    @staticmethod
    def agendar_chamada_aberta(id_chamada):

        chamada_aberta = Chamada.query.get(id_chamada)
        chamada_aberta.status = True
        db.session.merge(chamada_aberta)
        db.session.commit()
        print("Chamada aberta registrada!")