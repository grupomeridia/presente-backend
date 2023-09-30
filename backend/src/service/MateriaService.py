from repository.MateriaRepository import MateriaRepository

from entity.Materia import Materia


class MateriaService():
    @staticmethod
    def get_by_id(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("O ID deve ser um número inteiro")
        
        assert int(id) > 0, "ID inválido"
        assert Materia.query.get(id) != None, f"Nenhuma materia com o ID {id} foi encontrado"
        return MateriaRepository.get_materia_by_id(id)
    
    @staticmethod
    def register(materia_dto):

        materia = MateriaService.to_entity(materia_dto)

        return MateriaRepository.register(Materia(status=materia.status, nome=materia.nome))
    
    @staticmethod
    def update(id, materia):

        materia = MateriaService.to_entity(id, materia)

        return MateriaRepository.update(id, materia)
    
    @staticmethod
    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro.")
        
        assert int(id) > 0, "ID inválido"
        assert Materia.query.filter(Materia.id_materia == id).first() is not None, "Matéria não encontrada."
        return MateriaRepository.delete(id)
    
    @staticmethod
    def to_entity(materia_dto):
        materia = Materia(status=materia_dto.status, nome=materia_dto.nome)

        return materia