from flask import jsonify
from models import db
from datetime import datetime, timedelta
from entity.Professor import Professor
from entity.Aluno import Aluno
from entity.Turma import Turma
from entity.TurmaProfessor import turma_professor
from entity.TurmaAluno import turma_aluno
from entity.Chamada import Chamada
from entity.Presenca import Presenca

class ProfessorRepository():
    @staticmethod
    def get_professor_by_id(id):
        try:
            return {
                "id_professor": Professor.query.get(id).id_professor,
                "id_usuario" : Professor.query.get(id).id_usuario,
                "nome": Professor.query.get(id).nome,
                "status": Professor.query.get(id).status
            }
        except AttributeError as error:
            raise AssertionError ("Professor não existe.")
    
    @staticmethod
    def list_all():
        professores = Professor.query.all()
        resultado = [{
            'id': p.id_professor, 
            'id_usuario': p.id_usuario,
            'Nome': p.nome, 
            'Ativo': p.status
        } for p in professores]

        return jsonify(resultado)
    
    @staticmethod
    def update(id, data):
        professor = Professor.query.get(id)

        professor.id_usuario = data.id_usuario
        professor.nome = data.nome
        professor.status = data.status

        db.session.merge(professor)
        db.session.commit()
        return f"Professor ID {id} atualizado"
  
    @staticmethod
    def delete(id):
        professor = Professor.query.get(id)
        professor.status = False
        
        db.session.merge(professor)
        db.session.commit()


        return f"Professor ID {id} deletado com sucesso"
    
    @staticmethod
    def register(professor):

        db.session.add(professor)
        db.session.commit()
        
        return f"Professor cadastrado com o id {professor.id_professor}"
    
    @staticmethod
    def listar_turmas(id):
        consulta_sql = db.text("""
        SELECT t.*
        FROM turmas t
        JOIN turma_professor tp ON t.id_turma = tp.id_turma
        JOIN professores p ON tp.id_professor = p.id_professor
        WHERE p.id_professor = :id;
        """)

        with db.engine.connect() as connection:
            resultado = connection.execute(consulta_sql, {'id': id})
            resultado_dict = resultado.fetchall()

        resultado_json = []
        for id_turma, id_materia, status, nome, ano, semestre, turno, modalidade, curso in resultado_dict:
            resultado_json.append({
                'id_turma': id_turma, 
                'id_materia': id_materia,
                'status' : status,
                'nome': nome,
                'ano': ano,
                'semestre': semestre,
                'turno': turno,
                'modalidade': modalidade,
                'curso': curso
            })

        return resultado_json
    
    @staticmethod
    def num_alunos(professor_id, chamada_id):
        consulta_sql = db.text("""
        SELECT
            COUNT(ta.id_aluno) AS quantidade_alunos,
            SUM(CASE WHEN p.horario IS NOT NULL THEN 1 ELSE 0 END) AS alunos_presentes,
            SUM(CASE WHEN p.horario IS NULL THEN 1 ELSE 0 END) AS alunos_nao_presenca
        FROM
            turma_aluno ta
        LEFT JOIN
            presencas p ON ta.id_aluno = p.id_aluno AND p.id_chamada = :chamada_id
        LEFT JOIN
            turmas t ON t.id_turma = ta.id_turma
        LEFT JOIN
            turma_professor tp ON t.id_turma = tp.id_turma
        WHERE
            tp.id_professor = :professor_id
    """)

        with db.engine.connect() as connection:
            resultado = connection.execute(consulta_sql, {'professor_id': professor_id, 'chamada_id': chamada_id})
            resultado_dict = resultado.fetchone()

        quantidade_alunos = resultado_dict[0]
        alunos_presentes = resultado_dict[1]
        alunos_nao_presenca = resultado_dict[2]

        resultado_json = {
            "Total de Alunos": quantidade_alunos,
            "Faltam a chegar": alunos_nao_presenca,
            "Alunos presentes": alunos_presentes
        }

        return resultado_json
    
    @staticmethod
    def historico_semanal(turma_id):
        consulta_sql = db.text("""
            SELECT
                (SUM(CASE WHEN p.horario IS NOT NULL THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) AS porcentagem_presenca
            FROM
                turmas t
            LEFT JOIN
                turma_aluno ta ON t.id_turma = ta.id_turma
            LEFT JOIN
                presencas p ON ta.id_aluno = p.id_aluno
            WHERE
                t.id_turma = :turma_id
                AND (p.horario IS NULL OR p.horario >= NOW() - INTERVAL '7 days');

            """)
        
        with db.engine.connect() as connection:
            resultado = connection.execute(consulta_sql, {'turma_id': turma_id})
            porcentagem_presenca = resultado.scalar()

        resultado_json = {
            'porcentagem_presenca': porcentagem_presenca
        }
        
        return jsonify(resultado_json)
                
    @staticmethod
    def media_semanal(turma_id):
        consulta_sql = db.text("""
            SELECT
                EXTRACT(DOW FROM c.abertura) AS dia_semana,
                CASE
                    WHEN COUNT(p.id_aluno) > 0 THEN
                        ROUND(SUM(CASE WHEN p.horario IS NOT NULL THEN 1 ELSE 0 END) * 100.0 / COUNT(DISTINCT ta.id_aluno), 2)
                    ELSE
                        0
                END AS porcentagem_presenca
            FROM
                turma_aluno ta
            LEFT JOIN
                presencas p ON ta.id_aluno = p.id_aluno
            LEFT JOIN
                chamadas c ON p.id_chamada = c.id_chamada
            WHERE
                ta.id_turma = :turma_id
                AND c.abertura >= NOW() - INTERVAL '7 days'
            GROUP BY
                dia_semana
            ORDER BY
                dia_semana;
    """)

        with db.engine.connect() as connection:
            resultado = connection.execute(consulta_sql, {'turma_id': turma_id})
            resultados_dict = resultado.fetchall()

        resultado_json = []
        for dia_semana, porcentagem_presenca in resultados_dict:
            resultado_json.append({
                'dia_semana': int(dia_semana), 
                'porcentagem_presenca': porcentagem_presenca
            })

        return resultado_json

