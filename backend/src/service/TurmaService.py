from entity.Turma import Turma
from repository.TurmaRepository import TurmaRepository

class TurmaService():
    def getTurma(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("O ID deve ser um número inteiro.")

        assert int(id) > 0, "ID inválido"
        assert Turma.query.get(id) != None, f"Nenhuma turma com o ID {id} foi encontrada."
        return TurmaRepository.getTurmaById(id)
    
    def postTurma(ativo, nome, ano, semestre):
        try:
            int(ano)
            int(semestre)
        except ValueError:
            raise AssertionError("Os campos \"ano\" e \"semestre\" devem ser números inteiros ")
        assert ativo != None and ativo == True or False, "O campo ativo deve ser True ou False"
        assert len(str(nome)) >= 1 and nome != None, "Nome inválido"
        assert int(ano) > 2022 and int(ano) < 2100, "Ano inválido"
        assert semestre != None and int(semestre) > 0 and int(semestre) < 9, "Semestre inválido"  

        return TurmaRepository.register(Turma(ativo, nome, ano, semestre))