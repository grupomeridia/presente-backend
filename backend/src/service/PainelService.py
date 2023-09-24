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
        assert Aluno.query.get(id) != None, "Nenhum painel com este ID foi encontrado."

        return PainelRepository.getPainelById(id)
    
    def register(painelDTO):

        painel = PainelService.toEntity(painelDTO)

        return PainelRepository.registerPainel(Painel(painel.data, painel.totalAtivos, painel.totalPresentes, painel.totalAusentes, painel.totalPresentesCurso, painel.totalAtivoCurso, painel.totalAusenteCurso))
    
    def update(id, painel):
        
        painel = PainelService.toEntity(id, painel)

        return PainelRepository.update(id, painel)
    
    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID de ser um número inteiro.")
        
        assert int(id) > 0, "ID inválido."
        assert Painel.query.filter(Painel.id == id).first() is not None, "Painel não encontrado."
        return PainelRepository.delete(id)
    
    def toEntity(data):
        painel = Painel()
        painel.data = data.data
        painel.totalAtivos = data.totalAtivos
        painel.totalPresentes = data.totalPresentes
        painel.totalAusentes = data.totalAusentes
        painel.totalPresentesCurso = data.totalPresentesCurso
        painel.totalAtivoCurso = data.totalAtivoCurso
        painel.totalAusenteCurso = data.totalAusenteCurso

        return painel