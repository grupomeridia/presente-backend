from flask import jsonify
from repository.MainRepository import MainRepository
import datetime
from entity.Professor import Professor
from entity.Aluno import Aluno
from entity.Turma import Turma
from entity.TurmaProfessor import turma_professor
from entity.TurmaAluno import turma_aluno
from entity.Chamada import Chamada
from entity.Presenca import Presenca

class ProfessorRepository():
    def getProfessorById(id):
        return {
            "Id": Professor.query.get(id).id,
            "Nome": Professor.query.get(id).nome,
            "Ativo": Professor.query.get(id).ativo
        }
    
    def listAll():
        professores = Professor.query.all()
        resultado = [{
            'Id': p.id, 
            'Nome': p.nome, 
            'Ativo': p.ativo
        } for p in professores]

        return jsonify(resultado)
    
    def update(id, data):
        professor = Professor.query.get(id)

        professor.idUsuario = data.idUsuario
        professor.nome = data.status
        professor.ativo = data.nome

        MainRepository.db.session.merge(professor)
        MainRepository.db.session.commit()
        return f"Professor ID {id} atualizado"
  
    def delete(id):
        professor = Professor.query.get(id)
        professor.ativo = False
        
        MainRepository.db.session.merge(professor)
        MainRepository.db.session.commit()


        return f"Professor ID {id} deletado com sucesso"
    
    def register(professor):

        MainRepository.db.session.add(professor)
        MainRepository.db.session.commit()
        
        return f"Professor cadastrado com o id {professor.id_professor}"
    
    def listarTurmas(id):
        turmas = MainRepository.db.session.query(Turma).join(turma_professor).filter(Professor.id == id).all()

        if turmas:
            resultado = [{
                'Nome': t.nome,
                'Ano': t.ano,
                'Semestre': t.semestre,
                'Turno': t.turno,
                'Modalidade': t.modalidade,
                'Curso': t.curso,
            } for t in turmas]
        else:
            return "Professor não está cadastrado em nenhuma turma"
        
    def numAlunos(professor_id, chamada_id):
        
        professor = Professor.query.get(professor_id)

        if professor:
            quantidade_alunos = MainRepository.db.session.query(MainRepository.db.func.count(Aluno.id_aluno)).\
                join(turma_aluno).\
                join(Turma).\
                join(turma_professor).\
                filter(turma_professor.c.id_professor == professor_id).scalar()
            
            alunos_presentes = MainRepository.db.session.query(MainRepository.db.func.count(Aluno.id_aluno)).\
                join(turma_aluno).\
                join(Turma).\
                join(turma_professor).\
                join(Chamada).\
                join(Presenca, MainRepository.db.and_(
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
        
    def historicoSemanal(idTurma):

        turma = MainRepository.db.session.query(Turma).filter_by(Turma.idTurma == idTurma).first()

        if turma:
            dataAtual = datetime.now()
            dataInicial = dataAtual - datetime.timedelta(days=4)

            historico = MainRepository.db.session.query(MainRepository.db.func.date(Presenca.c.horario).label("data"),
                                                        (MainRepository.db.func.count(Aluno.id)/
                                                          MainRepository.db.func.count().label("total_alunos")).label("porcetagem")).\
                join(Chamada).\
                join(turma_professor).\
                join(Turma).\
                join(turma_aluno).\
                join(Aluno).\
                filter(Turma.idTurma == idTurma).\
                filter(Presenca.c.horario >= dataInicial).\
                filter(Presenca.c.horario <= dataAtual).\
                group_by(MainRepository.db.func.date(Presenca.c.date)).all() 
            
            if historico:
                resultado = []
                for data, porcetagem in historico:
                    dataFormatada = data.strftime('%Y-%m-%d')
                    porcetagemFormatada = round(porcetagem * 100, 2)
                    resultado.append(f"Data: {dataFormatada}, Porcetagem: {porcetagemFormatada}%")

                resultadoComoString = ', '.join(resultado)
                return resultadoComoString
            
            else: 
                return "Nenhum dado de presença disponivel"

        else:
            return "Turma não encontrada"
        
    def mediaSemanal(idTurma):
        
        dataInicial = datetime.now() - datetime.timedelta(days=5)

        mediaFrequencia = MainRepository.db.session.query(
            MainRepository.db.func.avg(MainRepository.db.func.coalesce(MainRepository.db.func.count(Presenca.c.id), 0) /
                     MainRepository.db.func.count(Aluno.id)).label('media_frequencia')
            ).join(Turma).\
            join(turma_aluno).\
            join(Aluno).\
            outerjoin(Presenca, (
                Aluno.id == Presenca.c.idAluno) & (Chamada.id == Presenca.c.idChamada)).\
            filter(Turma.idTurma == idTurma).\
            filter(Chamada.abertura >= dataInicial).scalar()
        
        return {f"Media frequencia {mediaFrequencia * 100:.2f}"} 
