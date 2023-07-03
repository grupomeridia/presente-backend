from repository.AlunoRepository import AlunoRepository

from entity.Aluno import Aluno

class AlunoService():
    def getbyid(id):
        try: 
            int(id)
        except ValueError:
            raise AssertionError("Deve ser um número inteiro")

        assert int(id) > 0, "ID inválido."
        assert AlunoRepository.getAlunoById(id) != None, "Nenhum aluno com este ID foi encontrado."
        
        return AlunoRepository.getAlunoById(id)
    
    def register(ativo, nome, ra, turma_id, curso):
        
        assert ativo != None and ativo == True, "Propriedade ativo deve ser True ou False"
        assert len(nome) > 3 and type(nome) == str, "Nome inválido"
        assert ra > 500000 and ra < 999999, "RA fornecido é inválido"
        assert curso != None and len(curso) > 10, "Curso inválido"
        assert turma_id != None and turma_id > 0, "Turma inválida"
        assert Aluno.query.filter(Aluno.ra == ra).first() is None, "RA já registrado"

        return AlunoRepository.registerAluno(Aluno(ativo, nome, ra, turma_id, curso))
    
    def update(id, Aluno):
        try: 
            int(id)
        except ValueError:
            raise AssertionError("Deve ser um número inteiro")
        assert int(id) > 0, "ID inválido."
        assert Aluno.ativo != None and Aluno.ativo == True or False, "Propriedade ativo deve ser True ou False"
        assert len(Aluno.nome) > 3 and type(Aluno.nome) == str, "Nome inválido"
        assert Aluno.ra > 500000 and Aluno.ra < 999999, "RA fornecido é inválido"
        assert Aluno.curso != None and len(Aluno.curso) > 10, "Curso inválido"
        assert Aluno.turma != None and len(Aluno.turma) > 0, "Turma inválida"

        return AlunoRepository.update(id, Aluno)