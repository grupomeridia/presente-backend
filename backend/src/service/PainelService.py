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

        return PainelRepository.registerPainel(Painel(id_configuracao=painel.id_configuracao, id_secretaria=painel.id_secretaria, data=painel.data, totalAtivos=painel.totalAtivos, totalPresentes=painel.totalPresentes, totalAusentes=painel.totalAusentes, totalPresentesCurso=painel.totalPresentesCurso, totalAtivoCurso=painel.totalAtivoCurso, totalAusenteCurso=painel.totalAusenteCurso))
    
    def update(id, painelDTO):
        
        painel = PainelService.toEntity(id, painelDTO)

        return PainelRepository.update(id, painel)
    
    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID de ser um número inteiro.")
        
        assert int(id) > 0, "ID inválido."
        assert Painel.query.filter(Painel.id == id).first() is not None, "Painel não encontrado."
        return PainelRepository.delete(id)
    
    def toEntity(painelDto):
        painel = Painel(id_configuracao=painelDto.id_configuracao, id_secretaria=painelDto.id_secretaria, data=painelDto.data, totalAtivos=painelDto.totalAtivos, totalPresentes=painelDto.totalPresentes, totalAusentes=painelDto.totalAusentes, totalPresentesCurso=painelDto.totalPresentesCurso, totalAtivoCurso=painelDto.totalAtivoCurso, totalAusenteCurso=painelDto.totalAusenteCurso)

        return painel