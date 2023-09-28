from repository.LembreteRepository import LembreteRepository
from entity.Lembrete import Lembrete
from entity.CargoEnum import Cargo

class LembreteService():
    def getById(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro.")
        
        assert int(id) > 0, "ID inválido."
        assert Lembrete.query.get(id) != None, "Nenhum lembrete com este ID foi encontrado."
        
        return LembreteRepository.getLembreteById(id)
    
    def register(lembreteDTO):

        lembrete = LembreteService.toEntity(lembreteDTO)
        
        
        return LembreteRepository.registerLembrete(Lembrete(id_secretaria=lembrete.id_secretaria, destinatarioCargo=lembrete.destinatarioCargo, titulo=lembrete.titulo, mensagem=lembrete.mensagem, criacao=lembrete.criacao, visualizacao=lembrete.visualizacao))
    
    def update(id, lembreteDTO):

        lembrete = LembreteService.toEntity(id, lembreteDTO)

        
        return LembreteRepository.update(id, lembrete)
    
    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro.")
        
        assert int(id) > 0, "ID inválido"
        assert Lembrete.query.filter(Lembrete.id == id).first() is not None, "Aluno não encontrado."
        return LembreteRepository.delete(id)
    
    def toEntity(lembreteDto):
        lembrete = Lembrete(id_secretaria=lembreteDto.id_secretaria, destinatarioCargo=lembreteDto.destinatarioCargo, titulo=lembreteDto.titulo, mensagem=lembreteDto.mensagem, criacao=lembreteDto.criacao, visualizacao=lembreteDto.visualizacao)

        return lembrete