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