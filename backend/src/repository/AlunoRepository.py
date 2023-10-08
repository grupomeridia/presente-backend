from flask import jsonify
from models import db
from entity.Aluno import Aluno

class AlunoRepository():
    @staticmethod
    def get_aluno_by_id(id):
        return {
            "id": Aluno.query.get(id).id_aluno,
            "id_usuario" : Aluno.query.get(id).id_usuario,
            "Nome": Aluno.query.get(id).nome,
            "RA": Aluno.query.get(id).ra,
            "Ativo": Aluno.query.get(id).status,
            "Ausente": Aluno.query.get(id).ausente
        }
    
    @staticmethod
    def list_all():
        alunos = Aluno.query.all()
        resultado = [{
            "id": a.id_aluno,
            "id_usuario" : a.id_usuario,
            "Nome": a.nome,
            "RA": a.ra,
            "Ativo": a.status,
            "Ausente" : a.ausente
        } for a in alunos]

        return jsonify(resultado)
    
    @staticmethod
    def update(id, aluno):
        old_aluno = Aluno.query.get(id)

        old_aluno.status = aluno.status
        old_aluno.nome = aluno.nome
        old_aluno.ra = aluno.ra
        old_aluno.ausente = aluno.ausente

        db.session.merge(old_aluno)
        db.session.commit()

        return f"Aluno ID {id} atualizado"
    
    @staticmethod
    def delete(id):
        aluno = Aluno.query.get(id)
        aluno.status = False
        db.session.merge(aluno)
        db.session.commit()
        return f"Aluno ID {id} deletado"
    
    @staticmethod
    def find_by_ra(ra):
        aluno = Aluno.query.filter(Aluno.ra == ra).first()
        return {
            "Id": aluno.id_aluno,
            "id_usuario" : aluno.id_usuario,
            "Nome": aluno.nome,
            "RA": aluno.ra,
            "Ativo": aluno.status,
            "Ausente" : aluno.ausente
        }
        
    @staticmethod
    def register_aluno(aluno):

        db.session.add(aluno)
        db.session.commit()

        return f"Aluno registrado com o ID {aluno.id_aluno}"
    
    @staticmethod
    def ausentes_presentes(turma_id):
        consulta_sql = db.text("""
            SELECT
                ta.id_aluno,
                CASE
                    WHEN p.horario IS NOT NULL THEN 'Presente'
                    ELSE 'Ausente'
                END AS situacao
            FROM
                turma_aluno ta
            LEFT JOIN
                presencas p ON ta.id_aluno = p.id_aluno
            LEFT JOIN
                chamadas c ON p.id_chamada = c.id_chamada
            WHERE
                ta.id_turma = :turma_id
                AND DATE(c.abertura) = DATE(NOW())
        """)

        with db.engine.connect() as connection:
            resultado = connection.execute(consulta_sql, {'turma_id': turma_id})
            resultados_dict = resultado.fetchall()

        resultado_json = []
        for id_aluno, situacao in resultados_dict:
            resultado_json.append({
                'id_aluno': id_aluno,
                'situacao': situacao
            })

        return resultado_json

    @staticmethod
    def ativo_inativo(turma_id):
        consulta_sql = db.text("""
        SELECT
            ta.id_aluno,
            CASE
                WHEN a.status = 'true' THEN 'Ativo'
                WHEN a.status = 'false' THEN 'Inativo'
                ELSE 'Desconhecido'
            END AS situacao
        FROM turma_aluno ta
        JOIN alunos a ON ta.id_aluno = a.id_aluno
        WHERE ta.id_turma = :turma_id
    """)

        with db.engine.connect() as connection:
            resultado = connection.execute(consulta_sql, {'turma_id': turma_id})
            resultados_dict = resultado.fetchall()

        resultado_json = []
        for id_aluno, situacao in resultados_dict:
            resultado_json.append({
                'id_aluno': id_aluno,
                'situacao': situacao
            })

        return resultado_json
    
