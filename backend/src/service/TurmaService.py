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

        return TurmaRepository.register(Turma(turma.status, turma.nome, turma.ano, turma.semestre, turma.turno, turma.modalidade, turma.curso))
    
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
        turma = Turma()
        turma.status = turmaDto.status
        turma.nome = turmaDto.nome
        turma.ano = turmaDto.ano
        turma.semestre = turmaDto.semestre
        turma.turno = turmaDto.turno
        turma.modalidade = turmaDto.modalidade
        turma.curso = turmaDto.curso

        return turma