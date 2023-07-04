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
        assert PresencaRepository.getPresencaById(id) != None, "Nenhuma Presenca foi encontrada"
        
        assert PresencaRepository.getPresencaById(id)

    def register(ativo, aluno_ra, turma, projeto, chamada, professor, tipo_presenca, horario):
        
        assert not Chamada.query.filter(Chamada.ativo == True).first() is None, "Não existe nenhuma chamada aberta"
        
        try:
            int(turma) 
            int(projeto)
            int(chamada)
        except ValueError:
            raise AssertionError("Os valores de turma, projeto e chamada devem ser números inteiros.")
    
        try:
            int(aluno_ra)
        except ValueError:
            raise AssertionError("RA deve ser um número inteiro")

        assert int(aluno_ra) > 500000 and int(aluno_ra) < 999999, "RA inválido"
        assert Aluno.query.filter(Aluno.ra == aluno_ra).first() is not None, f"O RA {aluno_ra} não pertence a nenhum aluno"
        
        assert ativo != None and ativo == True, "Propriedade ativo deve ser True ou False" 
        assert Presenca.query.filter(Presenca.aluno_ra == aluno_ra, Presenca.chamada_id == chamada).first() is None, "Presença já realizada"
        assert int(turma) > 0, "Turma inválida"
        assert int(projeto) > 0, "Projeto inválido"
        assert int(chamada) > 0, "Chamada inválida"
        assert professor != None and professor > 0, "Professor inválido"
        assert tipo_presenca != None, "Tipo da presença inválida"
        
        
        return PresencaRepository.registerPresenca(Presenca(ativo, aluno_ra, turma, projeto, chamada, professor, tipo_presenca, horario))