from repository.ProfessorRepository import ProfessorRepository

from entity.Professor import Professor
from entity.Chamada import Chamada
from entity.Turma import Turma

class ProfessorService():
    def getById(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("Deve ser um número inteiro.")
        
        assert int(id) > 0, "ID inválido."
        assert Professor.query.get(id) != None, "Nenhum professor com este ID foi encontrado."

        return ProfessorRepository.getProfessorById(id)
    
    def register(professorDto):
        
        professor = ProfessorService.toEntity(professorDto)
        
        return ProfessorRepository.register(Professor(professor.idUsuario, professor.status, professor.nome))
    
    def update(id, professorDto):

        professor = ProfessorService.toEntity(professorDto)

        return ProfessorRepository.update(id, professor)
    
    def listarTurmas(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro")
        
        assert int(id) > 0, "ID inválido!"
        assert Professor.query.get(id) != None, f"Nenhum professor foi encontrado com esse id"
        return ProfessorRepository.listarTurmas(id)
    
    def numAlunos(idProfessor, idChamada):
        try:
            int(idProfessor)
            int(idChamada)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro")
        
        assert int(idProfessor) > 0, "ID inválido!"
        assert int(idChamada) > 0, "ID inválido!"
        assert Professor.query.get(id) != None, f"Nenhum professor foi encontrado com esse id"
        assert Chamada.query.get(id) != None, f"Nenhuma chamada foi encontrada com esse id"

        return ProfessorRepository.numAlunos(idProfessor, idChamada)
    
    def historicoSemanal(idTurma):
        try:
            int(idTurma)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro")
        
        assert int(idTurma) > 0, "ID inválido!"
        assert Turma.query.get(id) != None, f"Nenhuma turma foi encontrada com esse id"

        return ProfessorRepository.historicoSemanal(idTurma)
    
    def mediaSemanal(idTurma):
        try:
            int(idTurma)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro")
        
        assert int(idTurma) > 0, "ID inválido!"
        assert Turma.query.get(id) != None, f"Nenhum turma foi encontrada com esse id"

        return ProfessorRepository.mediaSemanal(idTurma)

    def toEntity(professorDto):
        professor = Professor()
        professor = professorDto.idUsuario
        professor = professorDto.status
        professor = professorDto.nome

        return professor