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
        
        return ConfiguracaoRepository.registerConfiguracao(Configuracao(configuracao.status, configuracao.alunoAusente, configuracao.inicioAula, configuracao.finalAula))
    
    def update(id, configuracao):

        configuracao = ConfiguracaoService.toEntity(id, configuracao)
        
        return ConfiguracaoRepository.update(id, configuracao)

    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro")

        assert int(id) > 0, "ID inválido"
        assert Configuracao.query.filter(Configuracao.id == id).first() is not None, "Configuracao não encontrada"
        return ConfiguracaoRepository.delete(id)
    
    def toEntity(data):
        configuracao = Configuracao()
        configuracao.status = data.status
        configuracao.alunoAusente = data.alunoAusente
        configuracao.inicioAula = data.inicioAula
        configuracao.finalAula = data.finalAula

        return configuracao