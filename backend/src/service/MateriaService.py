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

        assert ativo != None and ativo == True or False, "O campo ativo deve ser true ou false"
        assert len(str(nome)) > 5 and nome != None, "Nome inválido"

        return MateriaRepository.register(Materia(materia.ativo, materia.nome))
    
    def update(id, materia):

        materia = MateriaService.toEntity(id, materia)

        return MateriaRepository.update(id, materia)
    
    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro.")
        
        assert int(id) > 0, "ID inválido"
        assert Materia.query.filter(Materia.id == id).first() is not None, "Matéria não encontrada."
        return MateriaRepository.delete(id)
    
    def toEntity(data):
        materia = Materia()
        materia.ativo = data.ativo
        materia.nome = data.nome

        return materia