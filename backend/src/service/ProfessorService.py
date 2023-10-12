from repository.ProfessorRepository import ProfessorRepository

from entity.Usuario import Usuario
from entity.Professor import Professor
from entity.Chamada import Chamada
from entity.Turma import Turma
from entity.CargoEnum import Cargo

from dtos.ProfessorDTO import ProfessorDTO

class ProfessorService():
    @staticmethod
    def get_by_id(id):
        assert id != None, "Nenhum ID enviado"
        assert int(id) if isinstance(id, (int,str)) and id.isdigit() else None, "ID incorreto."
        assert int(id) > 0 and int(id) < 999999, "ID inválido."
        assert Professor.query.get(id) != None, "Nenhum professor com este ID foi encontrado."

        return ProfessorRepository.get_professor_by_id(id)
    
    @staticmethod
    def register(id_usuario, status, nome):

        assert nome != 'NOT_FOUND', "Campo 'nome' inexistente."
        assert id_usuario != 'NOT_FOUND', "Campo 'id_usuario' inexistente."

        assert int(id_usuario) if isinstance(id_usuario, (int,str)) and str(id_usuario).isdigit() else None, "ID inválido."
        assert int(id_usuario) > 0 and int(id_usuario) < 999999, "ID de usuário inválido."

        assert not Professor.query.filter(Professor.id_usuario == id_usuario).first(), "ID já cadastrado."

        usuario = Usuario.query.get(id_usuario)
        assert usuario != None, "Usuário não encontrado."
        assert usuario.cargo == Cargo.Professor, "Usuário não é um professor."
        assert usuario.login == nome, "O nome de usuário não existe."

        assert not Professor.query.filter(Professor.nome == nome).first(), "Nome já cadastrado"


        professor = ProfessorService.to_entity(ProfessorDTO(id_usuario=id_usuario, status=status, nome=nome))
        return ProfessorRepository.register(professor)
    
    @staticmethod
    def update(id_professor, status, nome):

        assert id_professor != 'NOT_FOUND', "Campo 'id_professor' inexistente."
        assert nome != 'NOT_FOUND', "Campo 'nome' inexistente."

        assert int(id_professor) if isinstance(id_professor, (int,str)) and str(id_professor).isdigit() else None, "ID inválido."
        assert int(id_professor) > 0 and int(id_professor) < 999999, "ID de usuário inválido."

        professor = Professor.query.get(id)
        assert professor != None, "Usuário não encontrado."


        professor = ProfessorService.to_entity(ProfessorDTO(id_professor=id_professor, status=status, nome=nome))

        return ProfessorRepository.update(id, professor)
    
    @staticmethod
    def delete(id):
        assert id != None, "Nenhum ID enviado."
        assert int(id) if isinstance(id, (int,str)) and id.isdigit() else None, "ID incorreto."
        assert int(id) > 0 and int(id) < 999999, "ID inválido."

        assert Professor.query.get(id) != None, "Nenhum ID encontrado."
        
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
        
        assert Turma.query.get(id_turma) != None, "Nenhuma turma foi encontrada com esse id"

        return ProfessorRepository.historico_semanal(id_turma)
    
    @staticmethod
    def media_semanal(id_turma):
        try:
            int(id_turma)
        except ValueError:
            raise AssertionError("id da turma está inválido")
        
        assert Turma.query.get(id_turma) != None, "Nenhum turma foi encontrada"

        return ProfessorRepository.media_semanal(id_turma)

    @staticmethod
    def to_entity(professor_dto):
        professor = Professor(id_usuario=professor_dto.id_usuario, status=professor_dto.status, nome=professor_dto.nome)
  
        return professor