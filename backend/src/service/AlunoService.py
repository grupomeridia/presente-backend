from repository.AlunoRepository import AlunoRepository

from entity.Aluno import Aluno

class AlunoService():
    @staticmethod
    def get_by_id(id):
        try: 
            int(id)
        except ValueError:
            raise AssertionError("Deve ser um número inteiro")

        assert int(id) > 0, "ID inválido."
        assert Aluno.query.get(id) != None, "Nenhum aluno com este ID foi encontrado."
        
        return AlunoRepository.get_aluno_by_id(id)
    
    @staticmethod
    def register(aluno_dto):

        aluno = AlunoService.to_entity(aluno_dto)
    
        return AlunoRepository.register_aluno(Aluno(id_usuario=aluno.id_usuario, status=aluno.status, ausente=aluno.ausente, nome=aluno.nome, ra=aluno.ra))
    
    @staticmethod
    def update(id, aluno_dto):

        aluno = AlunoService.to_entity(aluno_dto)
               
        return AlunoRepository.update(id, aluno)
    
    @staticmethod
    def delete(id):
        try: 
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro")
        
        assert int(id) > 0, "ID inválido"
        assert Aluno.query.filter(Aluno.id_aluno == id).first() is not None, "Aluno não encontrado"
        return AlunoRepository.delete(id)

    @staticmethod
    def get_by_ra(ra):
        try: 
            int(ra)
        except ValueError:
            raise AssertionError("RA deve ser um número inteiro")
        
        assert int(ra) > 500000 and int(ra) < 999999, "RA fornecido é inválido"
        assert Aluno.query.filter(Aluno.ra == ra).first() is not None, "Nenhum aluno encontrado"

        return AlunoRepository.find_by_ra(ra)
    
    @staticmethod
    def to_entity(aluno_dto):
        aluno = Aluno(id_usuario=aluno_dto.id_usuario, status=aluno_dto.status, ausente=aluno_dto.ausente, nome=aluno_dto.nome, ra=aluno_dto.ra)
   
        return aluno
    
    @staticmethod
    def ausentes_presentes(turma_id):
        try:
            int(turma_id)
        except ValueError:
            return AssertionError("Deve ser uma turma válida")
        
        return AlunoRepository.ausentes_presentes(turma_id)
    
    @staticmethod
    def ativo_inativo(turma_id):
        try:
            int(turma_id)
        except ValueError:
            return AssertionError("Deve ser uma turma com valor válido")
        
        return AlunoRepository.ativo_inativo(turma_id)
    