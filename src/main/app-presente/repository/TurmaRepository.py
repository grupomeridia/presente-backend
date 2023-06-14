from repository.MainRepository import MainRepository


from entity.Turma import Turma

class TurmaRepository():
    def getTurmaById(id):
        return {"Nome":Turma.query.get(id).nome,
               "ID:":Turma.query.get(id).id,
               "Ativo": Turma.query.get(id).ativo,
               "Ano": Turma.query.get(id).ano,
               "Semestre": Turma.query.get(id).semestre}
    
           