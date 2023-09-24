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

    def register(chamadaDTO):

        chamada = ChamadaService.toEntity(chamadaDTO)
        

        return ChamadaRepository.registerChamada(Chamada(chamada.idMateria, chamada.idTurma, chamada.idProfessor, chamada.status, chamada.abertura, chamada.encerramento))

    def update(id, chamada):

        chamada = ChamadaService.toEntity(id, chamada)
        
        return ChamadaRepository.update(id, chamada)
    
    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro.")
        
        assert int(id) > 0, "ID inválido"
        assert Chamada.query.filter(Chamada.id == id).first() is not None, "Chamada não encontrada." 
        return ChamadaRepository.delete(id) 
    
    def toEntity(data):
        chamada = Chamada()
        chamada.idMateria = data.idMateria
        chamada.idTurma = data.idTurma
        chamada.idProfessor = data.idProfessor
        chamada.status = data.status
        chamada.abertura = data.abertura
        chamada.encerramento = data.encerramento

        return chamada