from repository.SecretariaRepository import SecretariaRepository
from entity.Secretaria import Secretaria
from entity.Usuario import Usuario
from entity.CargoEnum import Cargo

class SecretariaService():
    @staticmethod
    def get_by_id(id):
        assert id != None, "Nenhum ID enviado."
        assert int(id) if isinstance(id, (int,str)) and id.isdigit() else None, "ID incorreto."
        assert int(id) > 0 and int(id) < 999999, "ID inválido."

        assert Secretaria.query.get(id) != None, "Nenhum ID encontrado."

        return SecretariaRepository.get_by_id(id)
        
    @staticmethod
    def register(secretaria_dto, id_usuario):

        secretaria = SecretariaService.to_entity(secretaria_dto)
        usuario = Usuario.query.get(id_usuario)

        assert secretaria.id_usuario != 'NOT_FOUND', "Campo 'id' inexistente."
        assert secretaria.nome != 'NOT_FOUND', "Campo 'nome' inexistente."

        assert isinstance(id_usuario, int), "O ID está incorreto."
        assert usuario is not None, "Usuário não encontrado."
        assert int(id_usuario) > 0, "ID de usuário inválido."

        assert usuario.cargo == Cargo.Secretaria, "Usuário não é uma secretaria."
        assert not Secretaria.query.filter(Secretaria.id_usuario == secretaria.id_usuario).first(), "ID já cadastrado."
        assert not Secretaria.query.filter(Secretaria.nome == secretaria.nome).first(), "Nome já cadastrado"
        assert usuario.login == secretaria_dto.nome, "O nome de usuário não existe."
    
            

        return SecretariaRepository.register_secretaria(Secretaria(id_usuario=id_usuario, status=secretaria_dto.status, nome=secretaria_dto.nome))

    
    @staticmethod
    def update(id, secretaria_dto):

        secretaria = SecretariaService.to_entity(secretaria_dto)

        return SecretariaRepository.update(id, secretaria)
    
    @staticmethod
    def delete(id):
        assert id != None, "Nenhum ID enviado."
        assert int(id) if isinstance(id, (int,str)) and id.isdigit() else None, "ID incorreto."
        assert int(id) > 0 and int(id) < 999999, "ID inválido."

        assert Secretaria.query.get(id) != None, "Nenhum ID encontrado."

        assert Secretaria.query.filter(Secretaria.id_secretaria == id).first() is not None, "Secretaria não encontrada"
        
        return SecretariaRepository.delete(id)
    
    @staticmethod
    def to_entity(secretaria_dto):
        secretaria = Secretaria(id_usuario=secretaria_dto.id_usuario, status=secretaria_dto.status, nome=secretaria_dto.nome)

        return secretaria