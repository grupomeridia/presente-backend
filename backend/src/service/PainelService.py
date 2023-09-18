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
    
    def register(data, totalAtivos, totalPresentes, totalAusentes, totalPresentesCurso, totalAtivoCurso, totalAusenteCurso):
        try:
            assert isinstance(data, datetime.datetime), "Data inválida"
            assert isinstance(totalAtivos, int), "TotalAtivos deve ser um número inteiro"
            assert isinstance(totalPresentes, int), "TotalPresentes deve ser um número inteiro"
            assert isinstance(totalAusentes, int), "TotalAusentes deve ser um número inteiro"
            assert isinstance(totalPresentesCurso, list), "TotalPresentesCurso deve ser uma lista"
            assert isinstance(totalAtivoCurso, list), "TotalAtivoCurso deve ser uma lista"
            assert isinstance(totalAusenteCurso, list), "TotalAusenteCurso deve ser uma lista"
        except AssertionError as error:
            raise AssertionError(f"Campos obrigatórios inválidos: {str(error)}")

        return PainelRepository.registerPainel(Painel(data, totalAtivos, totalPresentes, totalAusentes, totalPresentesCurso, totalAtivoCurso, totalAusenteCurso))
    
    def update(id, data, totalAtivos, totalPresentes, totalAusentes, totalPresentesCurso, totalAtivoCurso, totalAusenteCurso):
        try:
            assert isinstance(data, datetime.datetime), "Data inválida"
            assert isinstance(totalAtivos, int), "TotalAtivos deve ser um número inteiro"
            assert isinstance(totalPresentes, int), "TotalPresentes deve ser um número inteiro"
            assert isinstance(totalAusentes, int), "TotalAusentes deve ser um número inteiro"
            assert isinstance(totalPresentesCurso, list), "TotalPresentesCurso deve ser uma lista"
            assert isinstance(totalAtivoCurso, list), "TotalAtivoCurso deve ser uma lista"
            assert isinstance(totalAusenteCurso, list), "TotalAusenteCurso deve ser uma lista"
        except AssertionError as error:
            raise AssertionError(f"Campos obrigatórios inválidos: {str(error)}")

        return PainelRepository.update(id, Painel(data, totalAtivos, totalPresentes, totalAusentes, totalPresentesCurso, totalAtivoCurso, totalAusenteCurso))
    
    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID de ser um número inteiro.")
        
        assert int(id) > 0, "ID inválido."
        assert Painel.query.filter(Painel.id == id).first() is not None, "Painel não encontrado."
        return PainelRepository.delete(id)