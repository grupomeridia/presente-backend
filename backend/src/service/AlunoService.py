from repository.AlunoRepository import AlunoRepository

from entity.Aluno import Aluno
from entity.Usuario import Usuario
from entity.CargoEnum import Cargo

from dtos.AlunoDTO import AlunoDTO

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
    def register(id_usuario, status, nome, ra, ausente):

        assert id_usuario != 'NOT_FOUND', "Campo 'ID Usuário' inexistente."
        assert nome != 'NOT_FOUND', "Campo 'Nome inexistente."
        assert ra != 'NOT_FOUND', "Campo 'RA inexistente."
        
        
        assert int(id_usuario) if isinstance(id_usuario, (int,str)) and str(id_usuario).isdigit() else None, "ID do Usuário incorreto."
        assert int(id_usuario) > 0 and int(id_usuario) < 999999, "ID de usuário inválido."

        assert not Aluno.query.filter(Aluno.id_usuario == id_usuario).first(), "ID de usuário já cadastrado."
        assert not Aluno.query.filter(Aluno.ra == ra).first(), "RA já esta sendo usado."
        
        assert re.match(r'^\d+$', str(ra)), "O RA deve ter apenas números."
        assert ra >= 100000 and ra <= 999999, "RA inválido."

        
        usuario = Usuario.query.get(id_usuario)
        assert usuario is not None, "Usuário não encontrado."
        assert usuario.cargo == Cargo.Aluno, "Usuário não é um aluno."
        assert usuario.login == nome, "O nome de usuário não existe."

        aluno = AlunoService.to_entity(AlunoDTO(id_usuario=id_usuario, status=status, nome=nome, ra=ra, ausente=ausente))
        
        return AlunoRepository.register_aluno(aluno)
    
    @staticmethod
    def update(id_aluno, status, nome, ra, ausente):

        assert id_aluno != 'NOT_FOUND', "Campo 'ID Aluno' inexistente."
        assert nome != 'NOT_FOUND', "Campo 'Nome inexistente."
        assert ra != 'NOT_FOUND', "Campo 'RA inexistente."
        
        aluno_antigo = AlunoRepository.get_aluno_by_id(id_aluno)

        assert int(id_aluno) if isinstance(id_aluno, (int,str)) and str(id_aluno).isdigit() else None, "ID do Aluno incorreto."
        

        assert re.match(r'^\d+$', str(ra)), "O RA deve ter apenas números."
        assert ra >= 100000 and ra <= 999999, "RA inválido."

        aluno = AlunoService.to_entity(AlunoDTO(id_usuario=aluno_antigo['id_aluno'], status=status, nome=nome, ra=ra, ausente=ausente))
               
        return AlunoRepository.update(id_aluno, aluno)
    
    @staticmethod
    def delete(id):
        assert id != None, "Nenhum ID enviado."
        assert int(id) if isinstance(id, (int,str)) and id.isdigit() else None, "ID incorreto."
        assert int(id) > 0 and int(id) < 999999, "ID inválido."
        assert Aluno.query.get(id) != None, "Nenhum aluno com este ID foi encontrado."
        
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
    
    @staticmethod
    def media_ativo(turma_id):
        try:
            int(turma_id)
        except ValueError:
            return AssertionError("deve ser uma turma valida")
        
        return AlunoRepository.media_ativo(turma_id)
    
    @staticmethod
    def media_ausente(turma_id):
        
        try:
            int(turma_id)
        except ValueError:
            return AssertionError("deve ser uma turma com valor valido")
        
        return AlunoRepository.media_ausente(turma_id)
    
    @staticmethod
    def historico_presenca(id_aluno):
        try:
            int(id_aluno)
        except ValueError:
            return AssertionError("Deve ser um aluno com valor valido.")
        
        return AlunoRepository.historico_presenca(id_aluno)
    
    @staticmethod
    def presenca_falta(id_aluno):
        try:
            int(id_aluno)
        except ValueError:
            return AssertionError("Deve ser um aluno com valor valido.")
        
        return AlunoRepository.presenca_falta(id_aluno)
    
    @staticmethod
    def aluno_status(id_aluno):

        assert id_aluno != None, "Nenhum ID do aluno enviado."
        assert int(id_aluno) if isinstance(id_aluno, (int,str)) and str(id_aluno).isdigit() else None, "ID do Usuário incorreto."
        assert int(id_aluno) > 0 and int(id_aluno) < 999999, "ID do aluno inválido."
        assert Aluno.query.get(id_aluno) != None, "Nenhum aluno com este ID foi encontrado."

        return AlunoRepository.aluno_status(id_aluno)