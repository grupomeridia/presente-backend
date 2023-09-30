from repository.SecretariaRepository import SecretariaRepository
from entity.Secretaria import Secretaria

class SecretariaService():
    @staticmethod
    def get_by_id(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro.")
        
        assert int(id) > 0, "ID inválido."
        assert Secretaria.query.get(id) != None, "Nenhum ID encontrado."
        
    @staticmethod
    def register(secretaria_dto):

        secretaria = SecretariaService.to_entity(secretaria_dto)

        return SecretariaRepository.register_secretaria(Secretaria(id_usuario=secretaria.id_usuario, status=secretaria.status, nome=secretaria.nome))
    
    @staticmethod
    def update(id, secretaria_dto):

        secretaria = SecretariaService.to_entity(secretaria_dto)

        return SecretariaRepository.update(id, secretaria)
    
    @staticmethod
    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro.")

        assert int(id) > 0, "ID inválido"
        
        return SecretariaRepository.delete(id)
    
    @staticmethod
    def to_entity(secretaria_dto):
        secretaria = Secretaria(id_usuario=secretaria_dto.id_usuario, status=secretaria_dto.status, nome=secretaria_dto.nome)

        return secretaria