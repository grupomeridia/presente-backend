from repository.ConfiguracaoRepository import ConfiguracaoRepository
from entity.Configuracao import Configuracao
import datetime
class ConfiguracaoService():
    def getConfiguracaoById(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("Deve ser um número inteiro")
        
        assert int(id) > 0, "ID inválido."
        assert ConfiguracaoRepository.getConfiguracaoById(id) != None, "Nenhuma configuracao foi encontrada"

        return ConfiguracaoRepository.getConfiguracaoById(id)
    
    def register(configuracaoDTO):

        configuracao = ConfiguracaoService.toEntity(configuracaoDTO)
        
        return ConfiguracaoRepository.registerConfiguracao(Configuracao(status=configuracao.status, aluno_ausente=configuracao.aluno_ausente, inicio_aula=configuracao.inicio_aula, final_aula=configuracao.final_aula))
    
    def update(id, configuracao):

        configuracao = ConfiguracaoService.toEntity(id, configuracao)
        
        return ConfiguracaoRepository.update(id, configuracao)

    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro")

        assert int(id) > 0, "ID inválido"
        assert Configuracao.query.filter(Configuracao.id_configuracao == id).first() is not None, "Configuracao não encontrada"
        return ConfiguracaoRepository.delete(id)
    
    def toEntity(configuracaoDto):
        configuracao = Configuracao(status=configuracaoDto.status, aluno_ausente=configuracaoDto.aluno_ausente, inicio_aula=configuracaoDto.inicio_aula, final_aula=configuracaoDto.final_aula)

        return configuracao