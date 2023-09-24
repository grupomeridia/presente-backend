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
    
    def register(alunoDTO):

        aluno = AlunoService.toEntity(alunoDTO)
        
        assert ativo != None and ativo == True, "Propriedade ativo deve ser True ou False"
    

        return AlunoRepository.registerAluno(Aluno(aluno.idUsuario, aluno.ativo, aluno.nome, aluno.ra, aluno.turma_id, aluno.curso))
    
    def update(id, aluno):

        aluno = AlunoService.toEntity(id, aluno)
       
        assert ativo != None and ativo == False or True, "Propriedade ativo deve ser True ou False"
        
        return AlunoRepository.update(id, aluno)
    
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
    
    def toEntity(data):
        aluno = Aluno()
        aluno.idUsuario = data.idUsuario
        aluno.status = data.status
        aluno.ausente = data.ausente
        aluno.nome = data.nome
        aluno.ra = data.ra

        return aluno