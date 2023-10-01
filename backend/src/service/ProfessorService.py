from repository.ProfessorRepository import ProfessorRepository

from entity.Professor import Professor
from entity.Chamada import Chamada
from entity.Turma import Turma

class ProfessorService():
    @staticmethod
    def get_by_id(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("Deve ser um número inteiro.")
        
        assert int(id) > 0, "ID inválido."
        assert Professor.query.get(id) != None, "Nenhum professor com este ID foi encontrado."

        return ProfessorRepository.get_professor_by_id(id)
    
    @staticmethod
    def register(professor_dto):
        
        professor = ProfessorService.to_entity(professor_dto)
        
        return ProfessorRepository.register(Professor(id_usuario=professor.id_usuario, status=professor.status, nome=professor.nome))
    
    @staticmethod
    def update(id, professor_dto):

        professor = ProfessorService.to_entity(professor_dto)

        return ProfessorRepository.update(id, professor)
    
    @staticmethod
    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro.")
        
        assert Professor.query.filter(Professor.id_professor == id).first() is not None, "Professor não encontrado"

        return ProfessorRepository.delete(id)

    @staticmethod
    def listar_turmas(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("id inválido")
        
        assert Professor.query.get(id) != None, "Nenhum professor foi encontrado"
        return ProfessorRepository.listar_turmas(id)
    
    @staticmethod
    def num_alunos(id_professor, id_chamada):
        try:
            int(id_professor)
            int(id_chamada)
        except ValueError:
            raise AssertionError("id do professor ou da chamada inválidos")
        
        assert Professor.query.get(id_professor) != None, "Nenhum professor foi encontrado com esse id"
        assert Chamada.query.get(id_chamada) != None, "Nenhuma chamada foi encontrada com esse id"

        return ProfessorRepository.num_alunos(id_professor, id_chamada)
    
    @staticmethod
    def historico_semanal(id_turma):
        try:
            int(id_turma)
        except ValueError:
            raise AssertionError("id da turma inválido")
        
        assert Turma.query.get(id) != None, "Nenhuma turma foi encontrada com esse id"

        return ProfessorRepository.historico_semanal(id_turma)
    
    @staticmethod
    def media_semanal(id_turma):
        try:
            int(id_turma)
        except ValueError:
            raise AssertionError("id da turma está inválido")
        
        assert Turma.query.get(id) != None, "Nenhum turma foi encontrada"

        return ProfessorRepository.media_semanal(id_turma)

    @staticmethod
    def to_entity(professor_dto):
        professor = Professor(id_usuario=professor_dto.id_usuario, status=professor_dto.status, nome=professor_dto.nome)
  
        return professor