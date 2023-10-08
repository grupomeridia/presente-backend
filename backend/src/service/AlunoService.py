from repository.AlunoRepository import AlunoRepository

from entity.Aluno import Aluno
from entity.Usuario import Usuario
from entity.CargoEnum import Cargo
import re

class AlunoService():
    @staticmethod
    def get_by_id(id):
        assert id != None, "Nenhum ID enviado."
        assert int(id) if isinstance(id, (int,str)) and id.isdigit() else None, "ID incorreto."
        assert int(id) > 0 and int(id) < 999999, "ID inválido."
        assert Aluno.query.get(id) != None, "Nenhum aluno com este ID foi encontrado."
        
        return AlunoRepository.get_aluno_by_id(id)
    
    @staticmethod
    def register(aluno_dto, id_usuario):

        aluno = AlunoService.to_entity(aluno_dto)
        usuario = Usuario.query.get(id_usuario)

        assert isinstance(id_usuario, int), "O ID está incorreto."
        assert usuario is not None, "Usuário não encontrado."
        assert int(id_usuario) > 0, "ID de usuário inválido."

        assert usuario.cargo == Cargo.Aluno, "Usuário não é um aluno."
        assert not Aluno.query.filter(Aluno.id_usuario == aluno.id_usuario).first(), "ID já cadastrado."
        assert not Aluno.query.filter(Aluno.nome == aluno.nome).first(), "Nome já cadastrado"
        assert usuario.login == aluno_dto.nome, "O nome de usuário não existe."

        assert re.match(r'^\d+$', str(aluno.ra)), "O RA deve ter apenas números."
        assert aluno.ra >= 100000 and aluno.ra <= 999999, "RA inválido."
        

        return AlunoRepository.register_aluno(Aluno(id_usuario=id_usuario, status=aluno_dto.status, ausente=aluno_dto.ausente, nome=aluno_dto.nome, ra=aluno_dto.ra))
    
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