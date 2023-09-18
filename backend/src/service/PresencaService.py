from repository.PresencaRepository import PresencaRepository

from entity.Presenca import Presenca
from entity.Chamada import Chamada
from entity.Aluno import Aluno

class PresencaService():
    def getById(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("Deve ser um número inteiro")
        
        assert int(id) > 0, "ID inválido."
        assert Presenca.query.get(id) != None, f"Nenhuma presença foi encontrada com o ID {id}"
        assert PresencaRepository.getPresencaById(id)

    def register(idAluno, idChamada, status, tipo_presenca, horario):
        
        assert not Chamada.query.filter(Chamada.ativo == True).first() is None, "Não existe nenhuma chamada aberta"
        
        try:
            int(idAluno) 
            int(idChamada)
        except ValueError:
            raise AssertionError("Os valores de aluno, e chamada devem ser números inteiros.")
    
        assert status != None and status == True, "Propriedade ativo deve ser True ou False" 
        assert int(idAluno) > 0, "Aluno inválido"
        assert int(idChamada) > 0, "Chamada inválida"

        assert tipo_presenca != None, "Tipo da presença inválida"
        
        
        return PresencaRepository.registerPresenca(Presenca(idAluno, idChamada, status, tipo_presenca, horario))
    
    def update(id, data):
        
        try:
            int(id)
        except ValueError:
            raise AssertionError("Deve ser um número inteiro")

        return PresencaRepository.update(id, data)
    
    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("Deve ser um número inteiro")
        
        return PresencaRepository.delete(id)