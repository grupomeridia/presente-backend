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
        assert Presenca.query.get(id) != None, f"Nenhuma presença foi encontrada com o ID {id}"
        assert PresencaRepository.getPresencaById(id)

    def register(presencaDto):

        presenca = PresencaService.toEntity(presencaDto)
        
        assert not Chamada.query.filter(Chamada.ativo == True).first() is None, "Não existe nenhuma chamada aberta"
        
         
        return PresencaRepository.registerPresenca(Presenca(id_aluno=presenca.idAluno, id_chamada=presenca.idChamada, status=presenca.status, tipoPresenca=presenca.tipoPresenca, horario=presenca.horario))
    
    def update(id, presencaDto):
        
        presenca = PresencaService.toEntity(presencaDto)

        return PresencaRepository.update(id, presenca)
    
    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("Deve ser um número inteiro")
        
        return PresencaRepository.delete(id)
    
    def toEntity(alunoDto):
        presenca = Presenca(id_aluno=alunoDto.id_aluno, id_chamada=alunoDto.id_chamada, status=alunoDto.status, tipoPresenca=alunoDto.tipoPresenca, horario=alunoDto.horario)

        return presenca