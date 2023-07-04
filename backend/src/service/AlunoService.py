from repository.AlunoRepository import AlunoRepository

from entity.Aluno import Aluno

class AlunoService():
    def getbyid(id):
        try: 
            int(id)
        except ValueError:
            raise AssertionError("Deve ser um número inteiro")

        assert int(id) > 0, "ID inválido."
        assert Aluno.query.get(id) != None, "Nenhum aluno com este ID foi encontrado."
        
        return AlunoRepository.getAlunoById(id)
    
    def register(ativo, nome, ra, turma_id, curso):
        
        assert ativo != None and ativo == True, "Propriedade ativo deve ser True ou False"
        assert len(nome) > 3 and type(nome) == str, "Nome inválido"
        assert int(ra) > 500000 and int(ra) < 999999, "RA fornecido é inválido"
        assert curso != None and len(curso) > 10, "Curso inválido"
        assert int(turma_id) != None and int(turma_id) > 0, "Turma inválida"
        assert Aluno.query.filter(Aluno.ra == ra).first() is None, "RA já registrado"

        return AlunoRepository.registerAluno(Aluno(ativo, nome, ra, turma_id, curso))
    
    def update(id, ativo, nome, ra, turma_id, curso):
        try: 
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro")
        assert int(id) > 0, "ID inválido."
        assert ativo != None and ativo == False or True, "Propriedade ativo deve ser True ou False"
        assert len(nome) > 3 and type(nome) == str, "Nome inválido"
        assert ra > 500000 and ra < 999999, "RA fornecido é inválido"
        assert curso != None and len(curso) > 10, "Curso inválido"
        assert turma_id != None and turma_id > 0, "Turma inválida"

        return AlunoRepository.update(id, Aluno(ativo, nome, ra, turma_id, curso))
    
    def delete(id):
        try: 
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro")
        
        assert int(id) > 0, "ID inválido"
        assert Aluno.query.filter(Aluno.id == id).first() is not None, "Aluno não encontrado"
        return AlunoRepository.delete(id)

    def getByRa(ra):
        try: 
            int(ra)
        except ValueError:
            raise AssertionError("RA deve ser um número inteiro")
        
        assert int(ra) > 500000 and int(ra) < 999999, "RA fornecido é inválido"
        assert Aluno.query.filter(Aluno.ra == ra).first() is not None, "Nenhum aluno encontrado"

        return AlunoRepository.findByRA(ra)