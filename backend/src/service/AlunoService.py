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

        #assert not Aluno.query.filter(Aluno.ra == aluno.ra).first(), "ra já está sendo usado"    
    
        return AlunoRepository.registerAluno(Aluno(id_usuario=aluno.id_usuario, status=aluno.status, ausente=aluno.ausente, nome=aluno.nome, ra=aluno.ra))
    
    def update(id, alunoDTO):

        aluno = AlunoService.toEntity(id, alunoDTO)
               
        return AlunoRepository.update(id, aluno)
    
    def delete(id):
        try: 
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro")
        
        assert int(id) > 0, "ID inválido"
        assert Aluno.query.filter(Aluno.id_aluno == id).first() is not None, "Aluno não encontrado"
        return AlunoRepository.delete(id)

    def getByRa(ra):
        try: 
            int(ra)
        except ValueError:
            raise AssertionError("RA deve ser um número inteiro")
        
        assert int(ra) > 500000 and int(ra) < 999999, "RA fornecido é inválido"
        assert Aluno.query.filter(Aluno.ra == ra).first() is not None, "Nenhum aluno encontrado"

        return AlunoRepository.findByRA(ra)
    
    def toEntity(alunoDto):
        aluno = Aluno(id_usuario=alunoDto.id_usuario, status=alunoDto.status, ausente=alunoDto.ausente, nome=alunoDto.nome, ra=alunoDto.ra)
   
        return aluno