from repository.ProfessorRepository import ProfessorRepository

from entity.Professor import Professor

class ProfessorService():
    def getProfessor(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro")
        
        assert int(id) > 0, "ID inválido!"
        assert Professor.query.get(id) != None, f"Nenhum professor foi encontrado com o ID {id}"
        return ProfessorRepository.getProfessorById(id)
    
    def postProfessor(ativo, nome):
        assert ativo != None and ativo == True or False, "Campo ativo deve ser True ou False" 
        assert len(str(nome)) > 3 and nome != None, "Nome inválido!"
        
        return ProfessorRepository.register(Professor(ativo, nome))