import datetime
from repository.PainelRepository import PainelRepository

from entity.Painel import Painel
from dtos.PainelDTO import PainelDTO
from entity.Configuracao import Configuracao
from entity.Secretaria import Secretaria

import re

class PainelService():
    @staticmethod
    def get_by_id(id):
        assert id != None, "Nenhum ID enviado."
        assert int(id) if isinstance(id, (int,str)) and id.isdigit() else None, "ID incorreto."
        assert int(id) > 0 and int(id) < 999999, "ID inválido."
        assert Painel.query.get(id) != None, "Nenhum painel com este ID foi encontrado."
        
        return PainelRepository.get_painel_by_id(id)
    
    @staticmethod
    def register(id_configuracao, id_secretaria, status, data_criado, total_ativo, total_ausentes, total_presentes, total_presentes_curso, total_ativo_curso, total_ausente_curso):

        assert id_configuracao != 'NOT_FOUND', "Campo 'id_configuracao' inexistente."
        assert id_secretaria != 'NOT_FOUND', "Campo 'id_secretaria' inexistente."
        assert total_ativo != 'NOT_FOUND', "Campo 'total_ativo' inexistente."
        assert total_presentes != 'NOT_FOUND', "Campo 'otal_presentes' inexistente."
        assert total_ausentes != 'NOT_FOUND', "Campo 'total_ausentes' inexistente."
        assert total_presentes_curso != 'NOT_FOUND', "Campo 'total_presentes_curso' inexistente."
        assert total_ativo_curso != 'NOT_FOUND', "Campo 'total_ativo_curso' inexistente."
        assert total_ausente_curso != 'NOT_FOUND', "Campo 'total_ausente_curso' inexistente."

        assert int(id_configuracao) if isinstance(id_configuracao, (int,str)) and str(id_configuracao).isdigit() else None, "ID de configuração incorreto."
        assert int(id_configuracao) > 0 and int(id_configuracao) < 999999, "ID de configuração inválido."
        assert re.match(r'^\d+$', str(id_configuracao)), "O ID de configuração deve ter apenas números."
        configuracao = Configuracao.query.get(id_configuracao)
        assert configuracao is not None, "Configuração não encontrada"

        assert int(id_secretaria) if isinstance(id_secretaria, (int,str)) and str(id_secretaria).isdigit() else None, "ID de secretaria incorreto."
        assert int(id_secretaria) > 0 and int(id_secretaria) < 999999, "ID de secretaria inválido."
        assert re.match(r'^\d+$', str(id_secretaria)), "O ID de secretaria deve ter apenas números."
        secretaria = Secretaria.query.get(id_secretaria)
        assert secretaria is not None, "Secretaria não encontrada"

        assert isinstance(total_ativo, int) and total_ativo >= 0, "O campo 'total_ativo' deve ser um número inteiro não negativo."
        assert isinstance(total_presentes, int) and total_presentes >= 0, "O campo 'total_presentes' deve ser um número inteiro não negativo."
        assert isinstance(total_ausentes, int) and total_ausentes >= 0, "O campo 'total_ausentes' deve ser um número inteiro não negativo."
        assert isinstance(total_presentes_curso, int) and total_presentes_curso >= 0, "O campo 'total_presentes_curso' deve ser um número inteiro não negativo."
        assert isinstance(total_ativo_curso, int) and total_ativo_curso >= 0, "O campo 'total_ativo_curso' deve ser um número inteiro não negativo."
        assert isinstance(total_ausente_curso, int) and total_ausente_curso >= 0, "O campo 'total_ausente_curso' deve ser um número inteiro não negativo."



        painel = PainelService.to_entity(PainelDTO(id_configuracao=id_configuracao, id_secretaria=id_secretaria, status=status, data_criado=data_criado, total_ativo=total_ativo, total_ausentes=total_ausentes, total_presentes=total_presentes, total_presentes_curso=total_presentes_curso, total_ativo_curso=total_ativo_curso, total_ausente_curso=total_ausente_curso))

        return PainelRepository.register_painel(painel)
    
    @staticmethod
    def update(id_painel,id_configuracao, id_secretaria, status, data_criado, total_ativo, total_ausentes, total_presentes, total_presentes_curso, total_ativo_curso, total_ausente_curso):
        
        assert id_painel != None, "Nenhum ID enviado."
        assert int(id_painel) if isinstance(id_painel, (int,str)) and id_painel.isdigit() else None, "ID incorreto."
        assert int(id_painel) > 0 and int(id_painel) < 999999, "ID inválido."
        assert Painel.query.get(id_painel) != None, "Nenhum painel com este ID foi encontrado."
        

        assert id_configuracao != 'NOT_FOUND', "Campo 'id_configuracao' inexistente."
        assert id_secretaria != 'NOT_FOUND', "Campo 'id_secretaria' inexistente."
        assert total_ativo != 'NOT_FOUND', "Campo 'total_ativo' inexistente."
        assert total_presentes != 'NOT_FOUND', "Campo 'otal_presentes' inexistente."
        assert total_ausentes != 'NOT_FOUND', "Campo 'total_ausentes' inexistente."
        assert total_presentes_curso != 'NOT_FOUND', "Campo 'total_presentes_curso' inexistente."
        assert total_ativo_curso != 'NOT_FOUND', "Campo 'total_ativo_curso' inexistente."
        assert total_ausente_curso != 'NOT_FOUND', "Campo 'total_ausente_curso' inexistente."

        assert int(id_configuracao) if isinstance(id_configuracao, (int,str)) and str(id_configuracao).isdigit() else None, "ID de configuração incorreto."
        assert int(id_configuracao) > 0 and int(id_configuracao) < 999999, "ID de configuração inválido."
        assert re.match(r'^\d+$', str(id_configuracao)), "O ID de configuração deve ter apenas números."
        configuracao = Configuracao.query.get(id_configuracao)
        assert configuracao is not None, "Configuração não encontrada"

        assert int(id_secretaria) if isinstance(id_secretaria, (int,str)) and str(id_secretaria).isdigit() else None, "ID de secretaria incorreto."
        assert int(id_secretaria) > 0 and int(id_secretaria) < 999999, "ID de secretaria inválido."
        assert re.match(r'^\d+$', str(id_secretaria)), "O ID de secretaria deve ter apenas números."
        secretaria = Secretaria.query.get(id_secretaria)
        assert secretaria is not None, "Secretaria não encontrada"

        assert isinstance(total_ativo, int) and total_ativo >= 0, "O campo 'total_ativo' deve ser um número inteiro não negativo."
        assert isinstance(total_presentes, int) and total_presentes >= 0, "O campo 'total_presentes' deve ser um número inteiro não negativo."
        assert isinstance(total_ausentes, int) and total_ausentes >= 0, "O campo 'total_ausentes' deve ser um número inteiro não negativo."
        assert isinstance(total_presentes_curso, int) and total_presentes_curso >= 0, "O campo 'total_presentes_curso' deve ser um número inteiro não negativo."
        assert isinstance(total_ativo_curso, int) and total_ativo_curso >= 0, "O campo 'total_ativo_curso' deve ser um número inteiro não negativo."
        assert isinstance(total_ausente_curso, int) and total_ausente_curso >= 0, "O campo 'total_ausente_curso' deve ser um número inteiro não negativo."


        painel = PainelService.to_entity(PainelDTO(id_configuracao=id_configuracao, id_secretaria=id_secretaria, status=status, data_criado=data_criado, total_ativo=total_ativo, total_ausentes=total_ausentes, total_presentes=total_presentes, total_presentes_curso=total_presentes_curso, total_ativo_curso=total_ativo_curso, total_ausente_curso=total_ausente_curso))

        return PainelRepository.update(id_painel, painel)
    
    @staticmethod
    def delete(id):
        assert id != None, "Nenhum ID enviado."
        assert int(id) if isinstance(id, (int,str)) and id.isdigit() else None, "ID incorreto."
        assert int(id) > 0 and int(id) < 999999, "ID inválido."
        assert Painel.query.get(id) != None, "Nenhum painel com este ID foi encontrado."

        return PainelRepository.delete(id)
    
    @staticmethod
    def to_entity(painel_dto):
        painel = Painel(id_configuracao=painel_dto.id_configuracao, id_secretaria=painel_dto.id_secretaria, status=painel_dto.status, data_criado=painel_dto.data_criado, total_ativo=painel_dto.total_ativo, total_presentes=painel_dto.total_presentes, total_ausentes=painel_dto.total_ausentes, total_presentes_curso=painel_dto.total_presentes_curso, total_ativo_curso=painel_dto.total_ativo_curso, total_ausente_curso=painel_dto.total_ausente_curso)

        return painel