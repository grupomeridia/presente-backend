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

    def register(idMateria, idTurma, idProfessor, status, abertura, encerramento):
        try:
            int(idMateria)
            int(idTurma)
            int(idProfessor)
        except ValueError as error:
            raise AssertionError("Campos obrigatório: Projeto, Professor e Turma")
        

        return ChamadaRepository.registerChamada(Chamada(idMateria, idTurma, idProfessor, status, abertura, encerramento))

    def update(id, idMateria, idTurma, idProfessor, status, abertura, encerramento):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro.")
        
        return ChamadaRepository.update(id, Chamada(idMateria, idTurma, idProfessor, status, abertura, encerramento))
    
    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro.")
        
        assert int(id) > 0, "ID inválido"
        assert Chamada.query.filter(Chamada.id == id).first() is not None, "Chamada não encontrada." 
        return ChamadaRepository.delete(id) 
    