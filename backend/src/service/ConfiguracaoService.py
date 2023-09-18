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
    
    def register(status, alunoAusente, inicioAula, finalAula):
        try:
            bool(status)
            int(alunoAusente)
            datetime(inicioAula)
            datetime(finalAula)
        except ValueError as error:
            raise AssertionError("Campos obrigatório: alunoAusente, inicioAula, finalAula")
        
        return ConfiguracaoRepository.registerConfiguracao(Configuracao(status, alunoAusente, inicioAula, finalAula))
    
    def update(id, status, alunoAusente, inicioAula, finalAula):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro")
        
        return ConfiguracaoRepository.update(id, Configuracao(status, alunoAusente, inicioAula, finalAula))

    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro")

        assert int(id) > 0, "ID inválido"
        assert Configuracao.query.filter(Configuracao.id == id).first() is not None, "Configuracao não encontrada"
        return ConfiguracaoRepository.delete(id)