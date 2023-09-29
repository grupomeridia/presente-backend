from repository.MateriaRepository import MateriaRepository

from entity.Materia import Materia


class MateriaService():
    def getById(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("O ID deve ser um número inteiro")
        
        assert int(id) > 0, "ID inválido"
        assert Materia.query.get(id) != None, f"Nenhuma materia com o ID {id} foi encontrado"
        return MateriaRepository.getMateriaById(id)
    
    def register(materiaDTO):

        materia = MateriaService.toEntity(materiaDTO)

        return MateriaRepository.register(Materia(status=materia.status, nome=materia.nome))
    
    def update(id, materia):

        materia = MateriaService.toEntity(id, materia)

        return MateriaRepository.update(id, materia)
    
    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro.")
        
        assert int(id) > 0, "ID inválido"
        assert Materia.query.filter(Materia.id_materia == id).first() is not None, "Matéria não encontrada."
        return MateriaRepository.delete(id)
    
    def toEntity(materiaDto):
        materia = Materia(status=materiaDto.status, nome=materiaDto.nome)

        return materia