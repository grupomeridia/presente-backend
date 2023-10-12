from repository.ConfiguracaoRepository import ConfiguracaoRepository
from entity.Configuracao import Configuracao
from dtos.ConfiguracaoDTO import ConfiguracaoDTO
from datetime import datetime



class ConfiguracaoService():
    @staticmethod
    def get_configuracao_by_id(id):
        assert id != None, "Nenhum ID enviado."
        assert int(id) if isinstance(id, (int,str)) and id.isdigit() else None, "ID incorreto."
        assert int(id) > 0 and int(id) < 999999, "ID inválido."
        assert Configuracao.query.get(id) != None, "Nenhuma configuração com este ID foi encontrado."
        
        return ConfiguracaoRepository.get_configuracao_by_id(id)
    
    @staticmethod
    def register(status, aluno_ausente, inicio_aula, fim_aula):

        assert aluno_ausente != 'NOT_FOUND', "Campo 'aluno_ausente' inexistente."
        assert inicio_aula != 'NOT_FOUND', "Campo 'inicio_aula' inexistente."
        assert fim_aula != 'NOT_FOUND', "Campo 'fim_aula' inexistente."

        inicio_aula = datetime.strptime(inicio_aula, "%Y-%m-%d %H:%M:%S")
        fim_aula = datetime.strptime(fim_aula, "%Y-%m-%d %H:%M:%S")
        assert isinstance(aluno_ausente, int) and aluno_ausente > 0, "Valor incorreto ausências do aluno."
        assert isinstance(inicio_aula, datetime), "O campo 'inicio_aula' deve ser uma data e hora válida."
        assert isinstance(fim_aula, datetime), "O campo 'fim_aula' deve ser uma data e hora válida."

        assert fim_aula > inicio_aula, "A data e hora de término da aula deve ser posterior à data e hora de início."

        configuracao = ConfiguracaoService.to_entity(ConfiguracaoDTO(status=status, aluno_ausente=aluno_ausente, inicio_aula=inicio_aula, fim_aula=fim_aula))
        
        return ConfiguracaoRepository.register(configuracao)
    
    @staticmethod
    def update(id_configuracao, status, aluno_ausente, inicio_aula, fim_aula):
        
        assert id_configuracao != None, "Nenhum ID enviado."
        assert int(id_configuracao) if isinstance(id_configuracao, (int,str)) and id_configuracao.isdigit() else None, "ID incorreto."
        assert int(id_configuracao) > 0 and int(id_configuracao) < 999999, "ID inválido."
        assert Configuracao.query.get(id_configuracao) != None, "Nenhuma configuração com este ID foi encontrado."
        
        assert id_configuracao != 'NOT_FOUND', "Campo 'id_configuração' inexistente."
        assert aluno_ausente != 'NOT_FOUND', "Campo 'aluno_ausente' inexistente."
        assert inicio_aula != 'NOT_FOUND', "Campo 'inicio_aula' inexistente."
        assert fim_aula != 'NOT_FOUND', "Campo 'fim_aula' inexistente."

        inicio_aula = datetime.strptime(inicio_aula, "%Y-%m-%d %H:%M:%S")
        fim_aula = datetime.strptime(fim_aula, "%Y-%m-%d %H:%M:%S")
        assert isinstance(aluno_ausente, int) and aluno_ausente > 0, "Valor incorreto ausências do aluno."
        assert isinstance(inicio_aula, datetime), "O campo 'inicio_aula' deve ser uma data e hora válida."
        assert isinstance(fim_aula, datetime), "O campo 'fim_aula' deve ser uma data e hora válida."

        assert fim_aula > inicio_aula, "A data e hora de término da aula deve ser posterior à data e hora de início."


        configuracao = ConfiguracaoService.to_entity(ConfiguracaoDTO(status=status, aluno_ausente=aluno_ausente, inicio_aula=inicio_aula, fim_aula=fim_aula))
        
        return ConfiguracaoRepository.update(id_configuracao, configuracao)

    @staticmethod
    def delete(id):
        
        assert id != None, "Nenhum ID enviado."
        assert int(id) if isinstance(id, (int,str)) and id.isdigit() else None, "ID incorreto."
        assert int(id) > 0 and int(id) < 999999, "ID inválido."
        assert Configuracao.query.get(id) != None, "Nenhuma configuração com este ID foi encontrado."

        return ConfiguracaoRepository.delete(id)
    
    @staticmethod
    def to_entity(configuracao_dto):
        configuracao = Configuracao(status=configuracao_dto.status, aluno_ausente=configuracao_dto.aluno_ausente, inicio_aula=configuracao_dto.inicio_aula, fim_aula=configuracao_dto.fim_aula)

        return configuracao