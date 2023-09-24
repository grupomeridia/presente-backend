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
        
        
        return LembreteRepository.registerLembrete(Lembrete(lembrete.destinatarioCargo, lembrete.titulo, lembrete.mensagem, lembrete.criacao, lembrete.visualizacao))
    
    def update(id, lembrete):

        lembrete = LembreteService.toEntity(id, lembrete)

        
        return LembreteRepository.update(id, lembrete)
    
    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro.")
        
        assert int(id) > 0, "ID inválido"
        assert Lembrete.query.filter(Lembrete.id == id).first() is not None, "Aluno não encontrado."
        return LembreteRepository.delete(id)
    
    def toEntity(data):
        lembrete = Lembrete()
        lembrete.destinatarioCargo = data.destinatarioCargo
        lembrete.titulo = data.titulo
        lembrete.mensagem = data.mensagem
        lembrete.criacao = data.criacao
        lembrete.visualizacao = data.visualizacao

        return lembrete