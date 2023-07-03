from repository.PresencaRepository import PresencaRepository

from entity.Presenca import Presenca
from entity.Chamada import Chamada

class PresencaService():
    def getById(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("Deve ser um número inteiro")
        
        assert int(id) > 0, "ID inválido."
        assert PresencaRepository.getPresencaById(id) != None, "Nenhuma Presenca foi encontrada"
        
        assert PresencaRepository.getPresencaById(id)

    def register(ativo, aluno_ra, turma, projeto, chamada, professor, tipo_presenca, horario):
        
        assert ativo != None and ativo == True, "Propriedade ativo deve ser True ou False"
        assert Presenca.query.filter(Presenca.aluno_ra == aluno_ra, Presenca.chamada_id == chamada).first() is None, "Presença já realizada"
        assert int(turma) != None and int(turma) > 0, "Turma inválida"
        assert int(projeto) != None and int(projeto) > 0, "Projeto inválido"
        assert int(chamada) != None and int(chamada) > 0, "Chamada inválida"
        assert professor != None and professor > 0, "Professor inválido"
        assert tipo_presenca != None, "Tipo da presença inválida"
        assert not Chamada.query.filter(Chamada.ativo == True).first() is None, "Não existe nenhuma chamada aberta"
    
        return PresencaRepository.registerPresenca(Presenca(ativo, aluno_ra, turma, projeto, chamada, professor, tipo_presenca, horario))