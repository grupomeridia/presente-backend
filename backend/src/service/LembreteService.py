from repository.LembreteRepository import LembreteRepository
from entity.Lembrete import Lembrete
from entity.CargoEnum import Cargo

class LembreteService():
    @staticmethod
    def get_by_id(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro.")
        
        assert int(id) > 0, "ID inválido."
        assert Lembrete.query.get(id) != None, "Nenhum lembrete com este ID foi encontrado."
        
        return LembreteRepository.get_lembrete_by_id(id)
    
    @staticmethod
    def register(lembrete_dto):

        lembrete = LembreteService.to_entity(lembrete_dto)
        
        
        return LembreteRepository.create(Lembrete(id_secretaria=lembrete.id_secretaria, destinatario_cargo=lembrete.destinatario_cargo, destinatario_id=lembrete.destinatario_id, titulo=lembrete.titulo, mensagem=lembrete.mensagem, criacao=lembrete.criacao, visualizacao=lembrete.visualizacao))
    
    @staticmethod
    def update(id, lembrete_dto):

        lembrete = LembreteService.to_entity(id, lembrete_dto)

        
        return LembreteRepository.update(id, lembrete)
    
    @staticmethod
    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro.")
        
        assert int(id) > 0, "ID inválido"
        assert Lembrete.query.filter(Lembrete.id_lembrete == id).first() is not None, "Aluno não encontrado."
        return LembreteRepository.delete(id)
    
    @staticmethod
    def to_entity(lembrete_dto):
        lembrete = Lembrete(id_secretaria=lembrete_dto.id_secretaria, destinatario_cargo=lembrete_dto.destinatario_cargo, destinatario_id=lembrete_dto.destinatario_id, titulo=lembrete_dto.titulo, mensagem=lembrete_dto.mensagem, criacao=lembrete_dto.criacao, visualizacao=lembrete_dto.visualizacao)

        return lembrete