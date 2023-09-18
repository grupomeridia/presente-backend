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
        professor.nome = data['nome']
        professor.ativo = data['ativo']


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
        
        return f"Professor cadastrado com o id {professor.id}"
    
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
        
    def numAlunos(idProfessor, idChamada):
        professor = MainRepository.db.session.query(Professor).filter_by(Professor.id == id).first()

        if professor:
            quantidade_alunos = MainRepository.db.session.query(func.count(Aluno.id)).\
                join(turma_aluno).\
                join(Turma).\
                join(turma_professor).\
                filter(turma_professor.idProfessor == id).scalar()
            
            alunos_presentes = MainRepository.db.session.query(func.count(Aluno.id)).\
                join(turma_aluno).\
                join(Turma).\
                join(turma_professor).\
                join(Chamada).\
                join(Presenca, and_(
                    Aluno.id == Presenca.c.idAluno,
                    Presenca.c.idChamada == idChamada)).\
                filter(turma_professor.idProfessor == Chamada.idProfessor).scalar()
                

            alunos_nao_presenca = quantidade_alunos - alunos_presentes

            return {
                "Total de Alunos": quantidade_alunos,
                "Faltam a chegar": alunos_nao_presenca
            }

        else:
            return "Professor não encontrado"
        
    def historicoSemanal(idTurma):

        turma = MainRepository.db.session.query(Turma).filter_by(Turma.idTurma == idTurma).first()

        if turma:
            dataAtual = datetime.now()
            dataInicial = dataAtual - datetime.timedelta(days=4)

            historico = MainRepository.db.session.query(func.date(Presenca.c.horario).label("data"),
                                                        (func.count(Aluno.id)/
                                                          func.count().label("total_alunos")).label("porcetagem")).\
                join(Chamada).\
                join(turma_professor).\
                join(Turma).\
                join(turma_aluno).\
                join(Aluno).\
                filter(Turma.idTurma == idTurma).\
                filter(Presenca.c.horario >= dataInicial).\
                filter(Presenca.c.horario <= dataAtual).\
                group_by(func.date(Presenca.c.date)).all() 
            
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
            func.avg(func.coalesce(func.count(Presenca.c.id), 0) /
                     func.count(Aluno.id)).label('media_frequencia')
            ).join(Turma).\
            join(turma_aluno).\
            join(Aluno).\
            outerjoin(Presenca, (
                Aluno.id == Presenca.c.idAluno) & (Chamada.id == Presenca.c.idChamada)).\
            filter(Turma.idTurma == idTurma).\
            filter(Chamada.abertura >= dataInicial).scalar()
        
        return {f"Media frequencia {mediaFrequencia * 100:.2f}"} 
