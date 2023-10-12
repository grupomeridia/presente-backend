from repository.LembreteRepository import LembreteRepository
from entity.Lembrete import Lembrete
from entity.CargoEnum import Cargo
from dtos. LembreteDTO import LembreteDTO
from entity.Secretaria import Secretaria
from entity.Usuario import Usuario

import re

class LembreteService():
    @staticmethod
    def get_by_id(id):
        assert id != None, "Nenhum ID enviado."
        assert int(id) if isinstance(id, (int,str)) and id.isdigit() else None, "ID incorreto."
        assert int(id) > 0 and int(id) < 999999, "ID inválido."
        assert Lembrete.query.get(id) != None, "Nenhum lembrete com este ID foi encontrado."
        
        return LembreteRepository.get_lembrete_by_id(id)
    
    @staticmethod
    def register(criacao, status, id_secretaria, destinatario_cargo, destinatario_id, titulo, mensagem):
            
        cargos = [x.value for x in Cargo]
        assert destinatario_cargo in cargos, "Cargo inválido"

        assert id_secretaria != 'NOT_FOUND', "Campo 'id_secretaria' inexistente."
        assert destinatario_cargo != 'NOT_FOUND', "Campo 'destinatario_cargo' inexistente."
        assert destinatario_id != 'NOT_FOUND', "Campo 'destinatario_id' inexistente."
        assert titulo != 'NOT_FOUND', "Campo 'titulo' inexistente."
        assert mensagem != 'NOT_FOUND', "Campo 'mensagem' inexistente."



        assert int(id_secretaria) if isinstance(id_secretaria, (int,str)) and str(id_secretaria).isdigit() else None, "ID de secretaria incorreto."
        assert int(id_secretaria) > 0 and int(id_secretaria) < 999999, "ID de secretaria inválido."
        assert re.match(r'^\d+$', str(id_secretaria)), "O ID de secretaria deve ter apenas números."
        secretaria = Secretaria.query.get(id_secretaria)
        assert secretaria is not None, "Secretaria não encontrado"

        assert int(destinatario_id) if isinstance(destinatario_id, (int,str)) and str(destinatario_id).isdigit() else None, "ID de destinatario incorreto."
        assert int(destinatario_id) > 0 and int(destinatario_id) < 999999, "ID de destinatario inválido."
        assert re.match(r'^\d+$', str(destinatario_id)), "O ID de destinatario deve ter apenas números."
        
        assert destinatario_id is not None, "Destinatario não encontrado"
        assert LembreteRepository.get_cargo(destinatario_cargo, destinatario_id) == destinatario_id, "Destinatario incorreto."


        lembrete = LembreteService.to_entity(LembreteDTO(criacao=criacao, status=status, id_secretaria=id_secretaria, destinatario_cargo=destinatario_cargo, destinatario_id=destinatario_id, titulo=titulo, mensagem=mensagem))
        
        return LembreteRepository.create(lembrete)
    
    @staticmethod
    def update(criacao, status, id_secretaria, destinatario_cargo, destinatario_id, titulo, mensagem):

        cargos = [x.value for x in Cargo]
        assert destinatario_cargo in cargos, "Cargo inválido"

        assert id != None, "Nenhum ID enviado."
        assert int(id) if isinstance(id, (int,str)) and id.isdigit() else None, "ID incorreto."
        assert int(id) > 0 and int(id) < 999999, "ID inválido."
        assert Lembrete.query.get(id) != None, "Nenhum lembrete com este ID foi encontrado."
        
        assert id_secretaria != 'NOT_FOUND', "Campo 'id_secretaria' inexistente."
        assert destinatario_cargo != 'NOT_FOUND', "Campo 'destinatario_cargo' inexistente."
        assert destinatario_id != 'NOT_FOUND', "Campo 'destinatario_id' inexistente."
        assert titulo != 'NOT_FOUND', "Campo 'titulo' inexistente."
        assert mensagem != 'NOT_FOUND', "Campo 'mensagem' inexistente."



        assert int(id_secretaria) if isinstance(id_secretaria, (int,str)) and str(id_secretaria).isdigit() else None, "ID de secretaria incorreto."
        assert int(id_secretaria) > 0 and int(id_secretaria) < 999999, "ID de secretaria inválido."
        assert re.match(r'^\d+$', str(id_secretaria)), "O ID de secretaria deve ter apenas números."
        secretaria = Secretaria.query.get(id_secretaria)
        assert secretaria is not None, "Secretaria não encontrado"

        assert int(destinatario_id) if isinstance(destinatario_id, (int,str)) and str(destinatario_id).isdigit() else None, "ID de destinatario incorreto."
        assert int(destinatario_id) > 0 and int(destinatario_id) < 999999, "ID de destinatario inválido."
        assert re.match(r'^\d+$', str(destinatario_id)), "O ID de destinatario deve ter apenas números."
        
        assert destinatario_id is not None, "Destinatario não encontrado"
        assert LembreteRepository.get_cargo(destinatario_cargo, destinatario_id) == destinatario_id, "Destinatario incorreto."



        lembrete = LembreteService.to_entity(LembreteDTO(criacao=criacao, status=status, id_secretaria=id_secretaria, destinatario_cargo=destinatario_cargo, destinatario_id=destinatario_id, titulo=titulo, mensagem=mensagem))

        return LembreteRepository.update(id, lembrete)
    
    @staticmethod
    def delete(id):
        
        assert id != None, "Nenhum ID enviado."
        assert int(id) if isinstance(id, (int,str)) and id.isdigit() else None, "ID incorreto."
        assert int(id) > 0 and int(id) < 999999, "ID inválido."
        assert Lembrete.query.get(id) != None, "Nenhum lembrete com este ID foi encontrado."
        

        return LembreteRepository.delete(id)
    
    @staticmethod
    def to_entity(lembrete_dto):
        lembrete = Lembrete(id_secretaria=lembrete_dto.id_secretaria, status=lembrete_dto.status, destinatario_cargo=lembrete_dto.destinatario_cargo, destinatario_id=lembrete_dto.destinatario_id, titulo=lembrete_dto.titulo, mensagem=lembrete_dto.mensagem, criacao=lembrete_dto.criacao, visualizacao=lembrete_dto.visualizacao)

        return lembrete