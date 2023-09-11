from repository.SecretariaRepository import SecretariaRepository
from entity.Secretaria import Secretaria

class SecretariaService():
    def getById(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro.")
        
        assert int(id) > 0, "ID inválido."
        assert Secretaria.query.get(id) != None, "Nenhum ID encontrado."
        
    def register(nome):
        return SecretariaRepository.registerSecretaria(Secretaria(nome))
    
    def update(nome):
        return SecretariaRepository.update(Secretaria(nome))
    
    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro.")

        assert int(id) > 0, "ID inválido"
        
        return SecretariaRepository.delete(id)