from repository.MainRepository import MainRepository

from entity.Aluno import Aluno

class AlunoRepository():
    def getAlunoById(id):
        return {
            "Nome": Aluno.query.get(id).nome,
            "ID": Aluno.query.get(id).ativo,
            "Ativo": Aluno.query.get(id).ra,
            "Turma": Aluno.query.get(id).turma_id,
            "Curso": Aluno.query.get(id).curso.value
        }
    
    def verificarPresencaAluno(ra, turma_id, data):
        data_formatada = datetime.strptime(data, '%Y-%m-%d').date()
        presenca = Presenca.query.filter_by(aluno_ra=ra, turma_id=turma_id, horario=data_formatada).first()
        
        return presenca is not None