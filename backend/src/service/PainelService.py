import datetime
from repository.PainelRepository import PainelRepository

from entity.Painel import Painel

class PainelService():
    @staticmethod
    def get_by_id(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("Deve ser um número inteiro.")
        
        assert int(id) > 0, "ID inválido."
        assert Painel.query.get(id) != None, "Nenhum painel com este ID foi encontrado."

        return PainelRepository.get_painel_by_id(id)
    
    @staticmethod
    def register(painel_dto):

        painel = PainelService.to_entity(painel_dto)

        return PainelRepository.register_painel(Painel(id_configuracao=painel.id_configuracao, id_secretaria=painel.id_secretaria, status=painel.status, data_criado=painel.data_criado, total_ativo=painel.total_ativo, total_presentes=painel.total_presentes, total_ausentes=painel.total_ausentes, total_presentes_curso=painel.total_presentes_curso, total_ativo_curso=painel.total_ativo_curso, total_ausente_curso=painel.total_ausente_curso))
    
    @staticmethod
    def update(id, painel_dto):
        
        painel = PainelService.to_entity(id, painel_dto)

        return PainelRepository.update(id, painel)
    
    @staticmethod
    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro.")
        
        assert int(id) > 0, "ID inválido."
        assert Painel.query.filter(Painel.id_painel == id).first() is not None, "Painel não encontrado."
        return PainelRepository.delete(id)
    
    @staticmethod
    def to_entity(painel_dto):
        painel = Painel(id_configuracao=painel_dto.id_configuracao, id_secretaria=painel_dto.id_secretaria, status=painel_dto.status, data_criado=painel_dto.data_criado, total_ativo=painel_dto.total_ativo, total_presentes=painel_dto.total_presentes, total_ausentes=painel_dto.total_ausentes, total_presentes_curso=painel_dto.total_presentes_curso, total_ativo_curso=painel_dto.total_ativo_curso, total_ausente_curso=painel_dto.total_ausente_curso)

        return painel