from repository.ConfiguracaoRepository import ConfiguracaoRepository
from entity.Configuracao import Configuracao

class ConfiguracaoService():
    @staticmethod
    def get_configuracao_by_id(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("Deve ser um número inteiro")
        
        assert int(id) > 0, "ID inválido."
        assert ConfiguracaoRepository.get_configuracao_by_id(id) != None, "Nenhuma configuracao foi encontrada"

        return ConfiguracaoRepository.get_configuracao_by_id(id)
    
    @staticmethod
    def register(configuracao_dto):

        configuracao = ConfiguracaoService.to_entity(configuracao_dto)
        
        return ConfiguracaoRepository.register(Configuracao(status=configuracao.status, aluno_ausente=configuracao.aluno_ausente, inicio_aula=configuracao.inicio_aula, final_aula=configuracao.final_aula))
    
    @staticmethod
    def update(id, configuracao):

        configuracao = ConfiguracaoService.to_entity(id, configuracao)
        
        return ConfiguracaoRepository.update(id, configuracao)

    @staticmethod
    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro")

        assert int(id) > 0, "ID inválido"
        assert Configuracao.query.filter(Configuracao.id_configuracao == id).first() is not None, "Configuracao não encontrada"
        return ConfiguracaoRepository.delete(id)
    
    @staticmethod
    def to_entity(configuracao_dto):
        configuracao = Configuracao(status=configuracao_dto.status, aluno_ausente=configuracao_dto.aluno_ausente, inicio_aula=configuracao_dto.inicio_aula, final_aula=configuracao_dto.final_aula)

        return configuracao