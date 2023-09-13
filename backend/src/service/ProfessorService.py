from repository.ProfessorRepository import ProfessorRepository

from entity.Professor import Professor
from entity.Chamada import Chamada
from entity.Turma import Turma

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