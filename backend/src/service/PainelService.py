import datetime
from repository.PainelRepository import PainelRepository

from entity.Painel import Painel

class PainelService():
    def getById(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("Deve ser um número inteiro.")
        
        assert int(id) > 0, "ID inválido."
        assert Painel.query.get(id) != None, "Nenhum painel com este ID foi encontrado."

        return PainelRepository.getPainelById(id)
    
    def register(painelDTO):

        painel = PainelService.toEntity(painelDTO)

        return PainelRepository.registerPainel(Painel(id_configuracao=painel.id_configuracao, id_secretaria=painel.id_secretaria, data_criado=painel.data_criado, total_ativos=painel.total_ativos, total_presentes=painel.total_presentes, total_ausentes=painel.total_ausentes, total_presentes_curso=painel.total_presentes_curso, total_ativo_curso=painel.total_ativo_curso, total_ausente_curso=painel.total_ausente_curso))
    
    def update(id, painelDTO):
        
        painel = PainelService.toEntity(id, painelDTO)

        return PainelRepository.update(id, painel)
    
    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID de ser um número inteiro.")
        
        assert int(id) > 0, "ID inválido."
        assert Painel.query.filter(Painel.id_painel == id).first() is not None, "Painel não encontrado."
        return PainelRepository.delete(id)
    
    def toEntity(painelDto):
        painel = Painel(id_configuracao=painelDto.id_configuracao, id_secretaria=painelDto.id_secretaria, data_criado=painelDto.data_criado, total_ativos=painelDto.total_ativos, total_presentes=painelDto.total_presentes, total_ausentes=painelDto.total_ausentes, total_presentes_curso=painelDto.total_presentes_curso, total_ativo_curso=painelDto.total_ativo_curso, total_ausente_curso=painelDto.total_ausente_curso)

        return painel