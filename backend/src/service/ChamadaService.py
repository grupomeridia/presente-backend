from repository.ChamadaRepository import ChamadaRepository

from entity.Chamada import Chamada
from entity.Turma import Turma
from entity.Professor import Professor
from entity.Materia import Materia
from dtos.ChamadaDTO import ChamadaDTO

import re

class ChamadaService():
    @staticmethod
    def get_by_id(id):
        assert id != None, "Nenhum ID enviado."
        assert int(id) if isinstance(id, (int,str)) and id.isdigit() else None, "ID incorreto."
        assert int(id) > 0 and int(id) < 999999, "ID inválido."
        assert Chamada.query.get(id) != None, "Chamada não encontrada." 

        return ChamadaRepository.get_chamada_by_id(id)

    @staticmethod
    def register(id_materia, id_turma, id_professor, status, abertura):

        assert id_turma != 'NOT_FOUND', "Campo 'id_turma' inexistente."
        assert id_professor != 'NOT_FOUND', "Campo 'id_professor' inexistente."
        assert id_materia != 'NOT_FOUND', "Campo 'id_materia' inexistente."

        assert int(id_materia) if isinstance(id_materia, (int,str)) and str(id_materia).isdigit() else None, "ID de matéria incorreto."
        assert int(id_materia) > 0 and int(id_materia) < 999999, "ID de matéria inválido."
        assert re.match(r'^\d+$', str(id_materia)), "O ID de matéria deve ter apenas números."
        materia = Materia.query.get(id_materia)
        assert materia is not None, "Matéria não encontrada"

        assert int(id_turma) if isinstance(id_turma, (int,str)) and str(id_turma).isdigit() else None, "ID do Turma incorreto."
        assert int(id_turma) > 0 and int(id_turma) < 999999, "ID de turma inválido."
        assert re.match(r'^\d+$', str(id_turma)), "O ID de turma deve ter apenas números."
        turma = Turma.query.get(id_turma)
        assert turma is not None, "Turma não encontrada"

        assert int(id_professor) if isinstance(id_professor, (int,str)) and str(id_professor).isdigit() else None, "ID de Professor incorreto."
        assert int(id_professor) > 0 and int(id_professor) < 999999, "ID de professor inválido."
        assert re.match(r'^\d+$', str(id_professor)), "O ID de professor deve ter apenas números."
        professor = Professor.query.get(id_professor)
        assert professor is not None, "Professor não encontrado"
        

        chamada = ChamadaService.to_entity(ChamadaDTO(id_materia=id_materia, id_professor=id_professor, id_turma=id_turma, status=status, abertura=abertura))

        return ChamadaRepository.register_chamada(chamada)

    @staticmethod
    def update(id_chamada, id_materia, id_turma, id_professor, status, abertura):

        assert id_chamada != 'NOT_FOUND', "Campo 'id_chamada' inexistente."
        assert id_turma != 'NOT_FOUND', "Campo 'id_turma' inexistente."
        assert id_professor != 'NOT_FOUND', "Campo 'id_professor' inexistente."
        assert id_materia != 'NOT_FOUND', "Campo 'id_materia' inexistente."

        assert int(id_materia) if isinstance(id_materia, (int,str)) and str(id_materia).isdigit() else None, "ID de matéria incorreto."
        assert int(id_materia) > 0 and int(id_materia) < 999999, "ID de matéria inválido."
        assert re.match(r'^\d+$', str(id_materia)), "O ID de matéria deve ter apenas números."
        

        assert int(id_turma) if isinstance(id_turma, (int,str)) and str(id_turma).isdigit() else None, "ID do Turma incorreto."
        assert int(id_turma) > 0 and int(id_turma) < 999999, "ID de turma inválido."
        assert re.match(r'^\d+$', str(id_turma)), "O ID de turma deve ter apenas números."
        

        assert int(id_professor) if isinstance(id_professor, (int,str)) and str(id_professor).isdigit() else None, "ID de Professor incorreto."
        assert int(id_professor) > 0 and int(id_professor) < 999999, "ID de professor inválido."
        assert re.match(r'^\d+$', str(id_professor)), "O ID de professor deve ter apenas números."
        

        assert id_chamada != None, "Nenhum ID enviado."
        assert int(id_chamada) if isinstance(id_chamada, (int,str)) and id_chamada.isdigit() else None, "ID incorreto."
        assert int(id_chamada) > 0 and int(id_chamada) < 999999, "ID inválido."
        assert Chamada.query.get(id) != None, "Chamada não encontrada." 

        chamada = ChamadaService.to_entity(ChamadaDTO(id_chamada=id_chamada, id_materia=id_materia, id_professor=id_professor, id_turma=id_turma, status=status, abertura=abertura))
        
        return ChamadaRepository.update(id, chamada)
    
    @staticmethod
    def delete(id):
        assert id != None, "Nenhum ID enviado."
        assert int(id) if isinstance(id, (int,str)) and id.isdigit() else None, "ID incorreto."
        assert int(id) > 0 and int(id) < 999999, "ID inválido."
        assert Chamada.query.get(id) != None, "Chamada não encontrada." 
        
        return ChamadaRepository.delete(id) 
    
    @staticmethod
    def to_entity(chamada_dto):
        chamada = Chamada(id_materia=chamada_dto.id_materia, id_turma=chamada_dto.id_turma, id_professor=chamada_dto.id_professor, status=chamada_dto.status, abertura=chamada_dto.abertura, encerramento=chamada_dto.encerramento)

        return chamada