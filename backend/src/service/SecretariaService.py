from repository.SecretariaRepository import SecretariaRepository
from entity.Secretaria import Secretaria
from entity.Usuario import Usuario
from entity.CargoEnum import Cargo

from dtos.SecretariaDTO import SecretariaDTO

class SecretariaService():
    @staticmethod
    def get_by_id(id):
        assert id != None, "Nenhum ID enviado."
        assert int(id) if isinstance(id, (int,str)) and id.isdigit() else None, "ID incorreto."
        assert int(id) > 0 and int(id) < 999999, "ID inválido."

        assert Secretaria.query.get(id) != None, "Nenhum ID encontrado."

        return SecretariaRepository.get_by_id(id)
        
    @staticmethod
    def register(id_usuario, status, nome):

        assert id_usuario != 'NOT_FOUND', "Campo 'id' inexistente."
        assert nome != 'NOT_FOUND', "Campo 'nome' inexistente."
 

        assert int(id_usuario) if isinstance(id_usuario, (int,str)) and str(id_usuario).isdigit() else None, "ID inválido."
        assert int(id_usuario) > 0 and int(id_usuario) < 999999, "ID de usuário inválido."

        assert not Secretaria.query.filter(Secretaria.id_usuario == id_usuario).first(), "ID já cadastrado."

        usuario = Usuario.query.get(id_usuario)
        assert usuario != None, "Usuário não encontrado."
        assert usuario.cargo == Cargo.Secretaria, "Usuário não é da secretaria."
        assert usuario.login == nome, "O nome de usuário não existe."

        
        assert not Secretaria.query.filter(Secretaria.nome == nome).first(), "Nome já cadastrado"
        

        secretaria = SecretariaService.to_entity(SecretariaDTO(id_usuario=id_usuario, status=status, nome=nome))

        return SecretariaRepository.register_secretaria(secretaria)

    
    @staticmethod
    def update(id_secretaria, nome, status):

        assert id_secretaria != 'NOT_FOUND', "Campo 'id' inexistente."
        assert nome != 'NOT_FOUND', "Campo 'nome' inexistente."
 

        assert int(id_secretaria) if isinstance(id_secretaria, (int,str)) and str(id).isdigit() else None, "ID inválido."
        assert int(id_secretaria) > 0 and int(id_secretaria) < 999999, "ID de usuário inválido."


        secretaria = Secretaria.query.get(id)
        assert secretaria != None, "Usuário não encontrado"

        
        secretaria = SecretariaService.to_entity(SecretariaDTO(status=status, nome=nome, id_usuario=id))

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