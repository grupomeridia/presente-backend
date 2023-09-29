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
        

        return ChamadaRepository.registerChamada(Chamada(id_materia=chamada.id_materia, id_turma=chamada.id_turma, id_professor=chamada.id_professor, status=chamada.status, abertura=chamada.abertura))

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
    
    def toEntity(chamadaDto):
        chamada = Chamada(id_materia=chamadaDto.id_materia, id_turma=chamadaDto.id_turma, id_professor=chamadaDto.id_professor, status=chamadaDto.status, abertura=chamadaDto.abertura, encerramento=chamadaDto.encerramento)

        return chamada