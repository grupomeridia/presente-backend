from repository.ChamadaRepository import ChamadaRepository

from entity.Chamada import Chamada

class ChamadaService():
    @staticmethod
    def get_by_id(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("Deve ser um número inteiro")
        
        assert int(id) > 0, "ID inválido."

        assert Chamada.query.filter(Chamada.id_chamada == id).first() is not None, "Chamada não encontrada." 

        return ChamadaRepository.get_chamada_by_id(id)

    @staticmethod
    def register(chamada_dto):

        chamada = ChamadaService.to_entity(chamada_dto)
        

        return ChamadaRepository.register_chamada(Chamada(id_materia=chamada.id_materia, id_turma=chamada.id_turma, id_professor=chamada.id_professor, status=chamada.status, abertura=chamada.abertura, encerramento=chamada.encerramento))

    @staticmethod
    def update(id, chamada):

        chamada = ChamadaService.to_entity(id, chamada)
        
        return ChamadaRepository.update(id, chamada)
    
    @staticmethod
    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro.")
        
        assert int(id) > 0, "ID inválido"
        assert Chamada.query.filter(Chamada.id_chamada == id).first() is not None, "Chamada não encontrada." 
        return ChamadaRepository.delete(id) 
    
    @staticmethod
    def to_entity(chamada_dto):
        chamada = Chamada(id_materia=chamada_dto.id_materia, id_turma=chamada_dto.id_turma, id_professor=chamada_dto.id_professor, status=chamada_dto.status, abertura=chamada_dto.abertura, encerramento=chamada_dto.encerramento)

        return chamada