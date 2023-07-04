from repository.ProjetoRepository import ProjetoRepository

from entity.Projeto import Projeto


class ProjetoService():
    def getProjeto(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("O ID deve ser um número inteiro")
        
        assert int(id) > 0, "ID inválido"
        assert Projeto.query.get(id) != None, f"Nenhum projeto com o ID {id} foi encontrado"
        return ProjetoRepository.getProjetoById(id)
    
    def postProjeto(ativo, nome):
        assert ativo != None and ativo == True or False, "O campo ativo deve ser true ou false"
        assert len(str(nome)) > 5 and nome != None, "Nome inválido"
        return ProjetoRepository.register(Projeto(ativo, nome))
