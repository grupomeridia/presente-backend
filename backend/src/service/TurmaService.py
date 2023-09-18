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
    
    def postTurma(status, nome, ano, semestre, turno, modalidade, curso):
        try:
            int(ano)
            int(semestre)
        except ValueError:
            raise AssertionError("Os campos \"ano\" e \"semestre\" devem ser números inteiros ")
        assert status != None and status == True or False, "O campo ativo deve ser True ou False"
        assert len(str(nome)) >= 1 and nome != None, "Nome inválido"
        assert int(ano) > 2022 and int(ano) < 2100, "Ano inválido"
        assert semestre != None and int(semestre) > 0 and int(semestre) < 9, "Semestre inválido"  

        return TurmaRepository.register(Turma(status, nome, ano, semestre, turno, modalidade, curso))
    
    def update(id, data):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro")
        
        return TurmaRepository.update(id, data)
    
    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("ID deve ser um número inteiro")
    
        assert int(id) > 0, "ID inválido"
        assert Turma.query.filter(Turma.id == id).first() is not None, "Turma não encontrada"
        return TurmaRepository.delete(id)        