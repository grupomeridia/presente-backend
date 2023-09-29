from flask import jsonify
from repository.MainRepository import MainRepository

from entity.Configuracao import Configuracao

class ConfiguracaoRepository():
    def getConfiguracaoById(id):
        return{
            "id": Configuracao.query.get(id).id_configuracao,
            "Status": Configuracao.query.get(id).status,
            "Alunos Ausentes": Configuracao.query.get(id).aluno_ausente,
            "Inicio Aula": Configuracao.query.get(id).inicio_aula,
            "Final Aula": Configuracao.query.get(id).final_aula
        }
    
    def listAll():
        configuracao = Configuracao.query.all()
        resultado = [{
            "Id": c.id_configuracao,
            "Status": c.status,
            "Alunos Ausentes": c.aluno_ausente,
            "Inicio Aula": c.inicio_aula,
            "Final Aula": c.final_aula  
          }for c in configuracao]
        
        return jsonify(resultado)
    
    def update (id, data):
        configuracao = Configuracao.query.get(id)

        configuracao.status = data.status
        configuracao.aluno_ausente = data.aluno_ausente
        configuracao.inicio_aula = data.inicio_aula
        configuracao.final_aula = data.final_aula

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
        MainRepository.db.session.add(Configuracao(status=status, aluno_ausente=alunoAusente, inicio_aula=inicioAula, final_aula=finalAula))
        MainRepository.db.session.commit()

        return "Configuracao criada com sucesso"