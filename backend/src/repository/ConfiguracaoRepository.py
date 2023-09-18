from flask import jsonify
from repository.MainRepository import MainRepository

from entity.Configuracao import Configuracao

class ConfiguracaoRepository():
    def getConfiguracaoById(id):
        return{
            "id": Configuracao.query.get(id).id,
            "Status": Configuracao.query.get(id).status,
            "Alunos Ausentes": Configuracao.query.get(id).alunoAusente,
            "Inicio Aula": Configuracao.query.get(id).inicioAula,
            "Final Aula": Configuracao.query.get(id).finalAula
        }
    
    def listAll():
        configuracao = Configuracao.query.all()
        resultado = [{
            "Id": c.id,
            "Status": c.status,
            "Alunos Ausentes": c.alunoAusente,
            "Inicio Aula": c.inicioAula,
            "Final Aula": c.finalAula  
          }for c in configuracao]
        
        return jsonify(resultado)
    
    def update (id, status, alunoAusente, inicioAula, finalAula):
        configuracao = Configuracao.query.get(id)

        configuracao.status = status
        configuracao.alunoAusente = alunoAusente
        configuracao.inicioAula = inicioAula
        configuracao.finalAula = finalAula

        MainRepository.db.session.merge(configuracao)
        MainRepository.db.session.commit()
        return {"mensagem":"sucesso"}
    
    def delete (id):
        configuracao = Configuracao.query.get(id)
        
        configuracao.ativo= False
        
        MainRepository.db.session.merge(configuracao)
        MainRepository.db.session.commit()
        
        return {"mensagem":"sucesso"}

    def register(status, alunoAusente, inicioAula, finalAula):
        MainRepository.db.session.add(Configuracao(status, alunoAusente, inicioAula, finalAula))
        MainRepository.db.session.commit()

        return "Configuracao criada com sucesso"