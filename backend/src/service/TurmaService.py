from entity.Turma import Turma
from repository.TurmaRepository import TurmaRepository

class TurmaService():
    @staticmethod
    def get_turma(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("O ID deve ser um número inteiro.")

        assert int(id) > 0, "ID inválido"
        assert Turma.query.get(id) != None, f"Nenhuma turma com o ID {id} foi encontrada."
        return TurmaRepository.get_turma_by_id(id)
    
    @staticmethod
    def post_turma(turma_dto):
        
        turma = TurmaService.to_entity(turma_dto)

        return TurmaRepository.register(Turma(status=turma.status, nome=turma.nome, ano=turma.ano, semestre=turma.semestre, turno=turma.turno, modalidade=turma.modalidade, curso=turma.curso))
    
    @staticmethod
    def update(id, turma_dto):
        
        turma = TurmaService.to_entity(turma_dto)
        
        return TurmaRepository.update(id, turma)
    
    @staticmethod
    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro")
    
        assert int(id) > 0, "ID inválido"
        assert Turma.query.filter(Turma.id_turma == id).first() is not None, "Turma não encontrada"
        return TurmaRepository.delete(id)
    
    @staticmethod
    def to_entity(turma_dto):
        turma = Turma(status=turma_dto.status, nome=turma_dto.nome, ano=turma_dto.ano, semestre=turma_dto.semestre, turno=turma_dto.turno, modalidade=turma_dto.modalidade, curso=turma_dto.curso)

        return turma