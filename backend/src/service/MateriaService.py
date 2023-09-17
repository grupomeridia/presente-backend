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
    
    def register(ativo, nome):

        assert ativo != None and ativo == True or False, "O campo ativo deve ser true ou false"
        assert len(str(nome)) > 5 and nome != None, "Nome inválido"

        return MateriaRepository.register(Materia(ativo, nome))
    
    def update(id, ativo, nome):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro")
        assert int(id) > 0, "ID inválido."

        return MateriaRepository.update(id, Materia(ativo, nome))
    
    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro.")
        
        assert int(id) > 0, "ID inválido"
        assert Materia.query.filter(Materia.id == id).first() is not None, "Matéria não encontrada."
        return MateriaRepository.delete(id)
    
