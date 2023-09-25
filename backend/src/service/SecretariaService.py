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
        
    def register(secretariaDto):

        secretaria = SecretariaService.toEntity(secretariaDto)

        return SecretariaRepository.registerSecretaria(Secretaria(secretaria.idUsuario, secretaria.status, secretaria.nome))
    
    def update(id, secretariaDto):

        secretaria = SecretariaService.toEntity(secretariaDto)

        return SecretariaRepository.update(id, secretaria)
    
    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro.")

        assert int(id) > 0, "ID inválido"
        
        return SecretariaRepository.delete(id)
    
    def toEntity(secretariaDto):
        secretaria = Secretaria()
        secretaria.idUsuario = secretariaDto.idUsuario
        secretaria.status = secretariaDto.status
        secretaria.nome = secretariaDto.nome

        return secretaria