from repository.ChamadaRepository import ChamadaRepository

from entity.Chamada import Chamada

class ChamadaService():
    def getById(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("Deve ser um número inteiro")
        
        assert int(id) > 0, "ID inválido."
        assert ChamadaRepository.getChamadaById(id) != None, "Nenhum aluno com este ID foi encontrado."

        return ChamadaRepository.getChamadaById(id)

    def register(ativo, projeto_id, professor_id, turma_id):

        assert ativo != None and ativo == True, "Propriedade ativo deve ser True ou False"
        assert int(projeto_id) > 0 and int(projeto_id) != None, "ID de projeto inválido."
        assert int(professor_id) > 0 and int(professor_id) != None, "ID de professor inválido."
        assert int(turma_id) > 0 and int(turma_id) != None, "ID de turma inválida."
        assert Chamada.query.filter(Chamada.ativo == True).first() is None, "Já existe uma chamada aberta nesse momento."

        return ChamadaRepository.registerChamada(Chamada(ativo, projeto_id, professor_id, turma_id))

    def chamadasAbertasAluno(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("Deve ser um número inteiro")
        
        assert int(id) > 0, "ID inválido."
        assert ChamadaRepository.getChamadaById(id) != None, "Nenhum aluno com este ID foi encontrado."
        
        return ChamadaRepository.getChamadasAbertasAluno(id)