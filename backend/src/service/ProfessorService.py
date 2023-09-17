from repository.ProfessorRepository import ProfessorRepository

from entity.Professor import Professor

class ProfessorService():
    def getById(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("Deve ser um número inteiro.")
        
        assert int(id) > 0, "ID inválido."
        assert Professor.query.get(id) != None, "Nenhum professor com este ID foi encontrado."

        return ProfessorRepository.getProfessorById(id)
    
    def register(idProfessor, idUsuario, ativo, nome):
        try:
            int(idProfessor)
            int(idUsuario)
        except ValueError as error:
            raise AssertionError("Campos obritório: Professor e usuário.")
        
        return ProfessorRepository.registerProfessor(Professor(idProfessor, idUsuario, ativo, nome))
    
    def update(id, idProfessor, idUsuario, ativo, nome):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro.")
        assert int(id) > 0, "ID inválido."

        return ProfessorRepository.update(id, Professor(idProfessor, idUsuario, ativo, nome))
    
    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro")
        assert int(id) > 0, "ID inválido."
        assert Professor.query.filter(Professor.id == id).first() is not None, "Professor não encontrado"
        return ProfessorRepository.delete(id)