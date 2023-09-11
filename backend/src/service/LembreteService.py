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
    
    def register(destinatarioCargo, titulo, mensagem, criacao, visualizacao):
        
        assert destinatarioCargo in [cargo.value for cargo in Cargo], "Cargo do destinatário inválido."
        
        return LembreteRepository.registerLembrete(Lembrete(destinatarioCargo, titulo, mensagem, criacao, visualizacao))
    
    def update(id, destinatarioCargo, titulo, mensagem, criacao, visualizacao):
        
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro.")
        
        assert destinatarioCargo in [cargo.value for cargo in Cargo], "Cargo do destinatário inválido."
        
        return LembreteRepository.update(id, Lembrete(destinatarioCargo, titulo, mensagem, criacao, visualizacao))
    
    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro.")
        
        assert int(id) > 0, "ID inválido"
        assert Lembrete.query.filter(Lembrete.id == id).first() is not None, "Aluno não encontrado."
        return LembreteRepository.delete(id)