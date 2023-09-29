from entity.Turma import Turma
from repository.TurmaRepository import TurmaRepository

class TurmaService():
    def getTurma(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("O ID deve ser um número inteiro.")

        assert int(id) > 0, "ID inválido"
        assert Turma.query.get(id) != None, f"Nenhuma turma com o ID {id} foi encontrada."
        return TurmaRepository.getTurmaById(id)
    
    def postTurma(turmaDto):
        
        turma = TurmaService.toEntity(turmaDto)

        return TurmaRepository.register(Turma(status=turma.status, nome=turma.nome, ano=turma.ano, semestre=turma.semestre, turno=turma.turno, modalidade=turma.modalidade, curso=turma.curso))
    
    def update(id, turmaDto):
        
        turma = TurmaService.toEntity(turmaDto)
        
        return TurmaRepository.update(id, turma)
    
    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro")
    
        assert int(id) > 0, "ID inválido"
        assert Turma.query.filter(Turma.id == id).first() is not None, "Turma não encontrada"
        return TurmaRepository.delete(id)
    
    def toEntity(turmaDto):
        turma = Turma(status=turmaDto.status, nome=turmaDto.nome, ano=turmaDto.ano, semestre=turmaDto.semestre, turno=turmaDto.turno, modalidade=turmaDto.modalidade, curso=turmaDto.curso)

        return turma