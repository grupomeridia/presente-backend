from flask import jsonify
from models import db
from entity.Aluno import Aluno
from datetime import datetime

class AlunoRepository():
    @staticmethod
    def get_aluno_by_id(id):
        try:
            return {
                "id_aluno": Aluno.query.get(id).id_aluno,
                "id_usuario" : Aluno.query.get(id).id_usuario,
                "nome": Aluno.query.get(id).nome,
                "ra": Aluno.query.get(id).ra,
                "ativo": Aluno.query.get(id).status,
                "ausente": Aluno.query.get(id).ausente
            }
        except AttributeError as error:
            raise AssertionError ("Aluno não existe.")
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
        SUM(CASE WHEN p.horario IS NOT NULL THEN 1 ELSE 0 END) AS presentes,
        (select count(a.id_aluno) from alunos a
        JOIN turma_aluno ta ON a.id_aluno = ta.id_aluno
        where ta.id_turma = :turma_id
        ) - SUM(CASE WHEN p.horario IS NOT NULL THEN 1 ELSE 0 END) AS ausentes
        FROM turma_aluno ta
        JOIN turmas t ON t.id_turma = ta.id_turma
        LEFT JOIN presencas p ON ta.id_aluno = p.id_aluno
        LEFT JOIN chamadas c ON p.id_chamada = c.id_chamada
        WHERE ta.id_turma = :turma_id AND c.status = true;
        """)

        with db.engine.connect() as connection:
            resultado = connection.execute(consulta_sql, {'turma_id': turma_id}).fetchone()

        presentes = resultado[0]
        ausentes = resultado[1]
        
        resultado_json = {
            'presentes': presentes,
            'ausentes': ausentes
        }
       
        return resultado_json

    @staticmethod
    def ativo_inativo(turma_id):
        consulta_sql = db.text("""
        SELECT
        SUM(CASE WHEN a.ausente = 'true' THEN 1 ELSE 0 END) as ausente,
        SUM(CASE WHEN a.ausente = 'false' THEN 1 ELSE 0 END) as frequente
        FROM turma_aluno ta
        JOIN alunos a ON ta.id_aluno = a.id_aluno
        WHERE ta.id_turma = :turma_id
    """)

        with db.engine.connect() as connection:
            resultado = connection.execute(consulta_sql, {'turma_id': turma_id})
            resultados_dict = resultado.fetchone()

        ausente = resultados_dict[0]
        frequente = resultados_dict[1]
        
        resultado_json = {
            'ausente': ausente,
            'frequente': frequente
        }

        return resultado_json
    
    @staticmethod
    def media_ativo(turma_id):
        consulta_sql = db.text("""
        SELECT 
        COUNT(*) * 100.0 / (SELECT COUNT(*) FROM turma_aluno WHERE id_turma = :turma_id) AS media_alunos_frequentes
        FROM turma_aluno 
        WHERE id_turma = :turma_id AND id_aluno IN (SELECT id_aluno FROM alunos WHERE ausente = 'false');
        """)

        with db.engine.connect() as connection:
            resultado = connection.execute(consulta_sql, {'turma_id': turma_id})
            media_alunos_ativos = resultado.scalar()

        return {
            'media_alunos_frequentes': media_alunos_ativos
        }

    @staticmethod
    def media_ausente(turma_id):
        consulta_presencas = db.text("""
        SELECT 
        SUM(CASE WHEN p.horario IS NOT NULL THEN 1 ELSE 0 END) AS presentes
        FROM turma_aluno ta
        JOIN turmas t ON t.id_turma = ta.id_turma
        LEFT JOIN presencas p ON ta.id_aluno = p.id_aluno
        LEFT JOIN chamadas c ON p.id_chamada = c.id_chamada
        WHERE ta.id_turma = 1 AND c.status = true;
        """)

        consulta_ausentes = db.text("""
        select  
        (select count(a.id_aluno) from alunos a
        JOIN turma_aluno ta ON a.id_aluno = ta.id_aluno
        where ta.id_turma = 1
        ) - SUM(CASE WHEN p.horario IS NOT NULL THEN 1 ELSE 0 END) AS ausentes
        FROM turma_aluno ta
        JOIN turmas t ON t.id_turma = ta.id_turma
        LEFT JOIN presencas p ON ta.id_aluno = p.id_aluno
        LEFT JOIN chamadas c ON p.id_chamada = c.id_chamada
        WHERE ta.id_turma = 1 AND c.status = true;
        """)

        with db.engine.connect() as connection:
            total_presencas = connection.execute(consulta_presencas, {'turma_id': turma_id}).scalar()
            total_ausentes = connection.execute(consulta_ausentes, {'turma_id': turma_id}).scalar()
            total_alunos = total_ausentes + total_presencas
            if total_presencas > 0:
                media_alunos_ausentes = (total_ausentes / total_alunos) * 100
            else:
                media_alunos_ausentes = 0

        return {
            'media_alunos_ausentes': media_alunos_ausentes
            }

    @staticmethod
    def historico_presenca(id_aluno):
        consulta_presencas = db.text("""
        SELECT p.id_presenca, a.nome, p.status, p.horario, p.tipo_presenca
        FROM presencas p
        LEFT JOIN alunos a ON p.id_aluno = a.id_aluno
        WHERE p.id_aluno = :id_aluno and p.horario is not null;
    """)
        
        with db.engine.connect() as connection:
            historico_aluno = connection.execute(consulta_presencas, {'id_aluno': id_aluno}).fetchall()
        
        historico_presenca = []

        for id_presenca, nome, status, horario, tipo_presenca in historico_aluno:
            horario = horario.strftime("%Y-%m-%d %H:%M:%S.%f")
            horario_formatado = datetime.strptime(horario, "%Y-%m-%d %H:%M:%S.%f").strftime("%d/%m/%Y")
            historico_presenca.append({
                'id_presenca': id_presenca,
                'nome': nome,
                'status': status,
                'horario': horario_formatado,
                'tipo_presenca': tipo_presenca
            })
        
        return historico_presenca

    @staticmethod
    def presenca_falta(id_aluno):
        consulta_sql = db.text("""
        SELECT a.nome AS nome_aluno,
        SUM(CASE WHEN p.horario IS NOT NULL THEN 1 ELSE 0 END) AS presencas,
        SUM(CASE WHEN p.horario IS NULL THEN 1 ELSE 0 END) AS faltas
        FROM alunos a
        LEFT JOIN presencas p ON a.id_aluno = p.id_aluno
        WHERE a.id_aluno = :id_aluno
        GROUP BY a.id_aluno, a.nome;
""")
        
        with db.engine.connect() as connection:
            presenca = connection.execute(consulta_sql, {'id_aluno': id_aluno}).fetchone()

        nome = presenca[0]
        presencas = presenca[1]
        faltas = presenca[2]

        presenca_falta = {
            'nome': nome,
            'presencas': presencas,
            'faltas': faltas
        }
        
        return presenca_falta
    
    @staticmethod
    def alunos_ausentes():
        consulta_sql = db.text(""" SELECT * FROM alunos where ausente is true """)

        with db.engine.connect() as connection:
            ausentes_alunos = connection.execute(consulta_sql).fetchall()

        alunos_ausentes = []

        for id_aluno, id_usuario, status, ausentes, nome, ra in ausentes_alunos:
            alunos_ausentes.append({
                'id_aluno': id_aluno,
                'id_usuario': id_usuario,
                'status': status,
                'ausentes': ausentes,
                'nome': nome,
                'ra': ra
            })

        return alunos_ausentes
    
    @staticmethod
    def alunos_presentes():
        consulta_sql = db.text("""
            SELECT a.* FROM alunos a
            JOIN presencas p ON a.id_aluno = p.id_aluno
            JOIN chamadas c ON c.id_chamada = p.id_chamada
            WHERE p.horario is not null
            AND c.abertura = (SELECT MAX(abertura) FROM chamadas)
            """)
        
        with db.engine.connect() as connection:
            presentes_alunos = connection.execute(consulta_sql).fetchall()

        alunos_presentes = []

        for id_aluno, id_usuario, status, ausentes, nome, ra in presentes_alunos:
            alunos_presentes.append({
                'id_aluno': id_aluno,
                'id_usuario': id_usuario,
                'status': status,
                'ausentes': ausentes,
                'nome': nome,
                'ra': ra
            })
        
        return alunos_presentes
    
    @staticmethod
    def alunos_a_chegar():
        consulta_sql = db.text(""" 
        SELECT a.*
        FROM alunos a
        WHERE a.id_aluno NOT IN (
            SELECT p.id_aluno
            FROM presencas p
            INNER JOIN chamadas c ON c.id_chamada = p.id_chamada
            WHERE c.abertura = (SELECT MAX(abertura) FROM chamadas)
            AND p.horario IS NOT NULL); 
        """)

        with db.engine.connect() as connection:
            alunos_chegar = connection.execute(consulta_sql).fetchall()

        alunos_a_chegar = []

        for id_aluno, id_usuario, status, ausentes, nome, ra in alunos_chegar:
            alunos_a_chegar.append({
                'id_aluno': id_aluno,
                'id_usuario': id_usuario,
                'status': status,
                'ausentes': ausentes,
                'nome': nome,
                'ra': ra
            })

        return alunos_a_chegar
    
    @staticmethod
    def aluno_status(id_aluno):
        consulta_sql = db.text(""" 
        SELECT a.id_aluno, a.status, a.nome, a.ra,
            t.curso,
            SUM(CASE WHEN p.horario IS NULL THEN 1 ELSE 0 END) AS faltas,
            (SUM(CASE WHEN p.horario IS NOT NULL THEN 1 ELSE 0 END) * 100) / 
            COUNT(*) AS frequencia
        FROM alunos a 
        JOIN presencas p ON p.id_aluno = a.id_aluno
        JOIN turma_aluno ta ON ta.id_aluno = a.id_aluno
        JOIN turmas t ON t.id_turma = ta.id_turma
        WHERE a.id_aluno = :id_aluno
        GROUP BY a.id_aluno, t.id_turma;
         """)
        
        with db.engine.connect() as connection:
            aluno = connection.execute(consulta_sql, {'id_aluno':id_aluno}).fetchone()

            id_aluno = aluno[0]
            status = aluno[1]
            nome = aluno[2]
            ra = aluno[3]
            curso = aluno[4]
            faltas = aluno[5]
            frequencia = aluno[6]

            aluno_status = {
                'id_aluno': id_aluno,
                'status': status,
                'nome': nome,
                'ra': ra,
                'curso': curso,
                'faltas': faltas,
                'frequencia': frequencia
            }

            return aluno_status
        
    @staticmethod
    def alunos_presenca_turma(turma_id):
        turma_presenca_sql = db.text("""
        SELECT t.id_turma,
        COUNT(CASE WHEN a.status = TRUE THEN 1 ELSE 0 END) AS presentes,
        COUNT(CASE WHEN a.status = FALSE THEN 1 ELSE 0 END) AS ausentes
        FROM turmas t
        JOIN turma_aluno ta ON t.id_turma = ta.id_turma
        JOIN alunos a ON ta.id_aluno = a.id_aluno
        WHERE t.id_turma = :turma_id
        GROUP BY t.id_turma;
        """)

        with db.engine.connect() as connection:
            turma = connection.execute(turma_presenca_sql, {'turma_id':turma_id}).fetchall()

            turma_presenca = []

            for id_turma, presentes, ausentes in turma:
                turma_presenca.append({
                    'id_turma': id_turma,
                    'presentes': presentes,
                    'ausentes': ausentes
                })
            return turma_presenca