from flask import jsonify
from models import db
import datetime
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
        return {
            "id": Professor.query.get(id).id_professor,
            "id_usuario" : Professor.query.get(id).id_usuario,
            "Nome": Professor.query.get(id).nome,
            "Ativo": Professor.query.get(id).status
        }
    
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
        professor.ativo = False
        
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
        turmas = db.session.query(Turma).join(turma_professor).filter(Professor.id == id).all()

        if turmas:
            resultado = [{
                'Nome': t.nome,
                'Ano': t.ano,
                'Semestre': t.semestre,
                'Turno': t.turno,
                'Modalidade': t.modalidade,
                'Curso': t.curso,
            } for t in turmas]
            return jsonify(resultado)
        else:
            return "Professor não está cadastrado em nenhuma turma"
    
    @staticmethod
    def num_alunos(professor_id, chamada_id):
        
        professor = Professor.query.get(professor_id)

        if professor:
            quantidade_alunos = db.session.query(db.func.count(Aluno.id_aluno)).\
                join(turma_aluno).\
                join(Turma).\
                join(turma_professor).\
                filter(turma_professor.c.id_professor == professor_id).scalar()
            
            alunos_presentes = db.session.query(db.func.count(Aluno.id_aluno)).\
                join(turma_aluno).\
                join(Turma).\
                join(turma_professor).\
                join(Chamada).\
                join(Presenca, db.and_(
                    Aluno.id_aluno == turma_aluno.c.id_aluno,
                    Presenca.id_aluno == turma_aluno.c.id_aluno,
                    Presenca.id_chamada == chamada_id)).\
                filter(turma_professor.c.id_professor == Chamada.id_professor).scalar()
                

            alunos_nao_presenca = quantidade_alunos - alunos_presentes

            return {
                "Total de Alunos": quantidade_alunos,
                "Faltam a chegar": alunos_nao_presenca,
                "Aluno presentes": alunos_presentes
            }

        else:
            return "Professor não encontrado"
    
    @staticmethod
    def historico_semanal(turma_id):

        turma = db.session.query(Turma).filter_by(Turma.id_turma == turma_id).first()

        if turma:
            data_atual = datetime.now()
            data_inicial = data_atual - datetime.timedelta(days=4)

            historico = db.session.query(db.func.date(Presenca.c.horario).label("data"),
                                                        (db.func.count(Aluno.id)/
                                                          db.func.count().label("total_alunos")).label("porcetagem")).\
                join(Chamada).\
                join(turma_professor).\
                join(Turma).\
                join(turma_aluno).\
                join(Aluno).\
                filter(Turma.id_turma == turma_id).\
                filter(Presenca.c.horario >= data_inicial).\
                filter(Presenca.c.horario <= data_atual).\
                group_by(db.func.date(Presenca.c.date)).all() 
            
            if historico:
                resultado = []
                for data, porcetagem in historico:
                    data_formatada = data.strftime('%Y-%m-%d')
                    porcetagem_formatada = round(porcetagem * 100, 2)
                    resultado.append(f"Data: {data_formatada}, Porcetagem: {porcetagem_formatada}%")

                resultado_como_string = ', '.join(resultado)
                return resultado_como_string
            
            else: 
                return "Nenhum dado de presença disponivel"

        else:
            return "Turma não encontrada"
        
    @staticmethod
    def media_semanal(turma_id):
        
        data_inicial = datetime.now() - datetime.timedelta(days=5)

        media_frequencia = db.session.query(
            db.func.avg(db.func.coalesce(db.func.count(Presenca.c.id), 0) /
                     db.func.count(Aluno.id)).label('media_frequencia')
            ).join(Turma).\
            join(turma_aluno).\
            join(Aluno).\
            outerjoin(Presenca, (
                Aluno.id == Presenca.c.idAluno) & (Chamada.id == Presenca.c.idChamada)).\
            filter(Turma.id_turma == turma_id).\
            filter(Chamada.abertura >= data_inicial).scalar()
        
        return {f"Media frequencia {media_frequencia * 100:.2f}"} 
