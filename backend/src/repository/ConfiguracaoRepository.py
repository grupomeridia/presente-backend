from flask import jsonify
from repository.MainRepository import MainRepository

from entity.Configuracao import Configuracao

class ConfiguracaoRepository():
    @staticmethod
    def get_configuracao_by_id(id):
        return{
            "id": Configuracao.query.get(id).id_configuracao,
            "Status": Configuracao.query.get(id).status,
            "Alunos Ausentes": Configuracao.query.get(id).aluno_ausente,
            "Inicio Aula": Configuracao.query.get(id).inicio_aula,
            "Final Aula": Configuracao.query.get(id).final_aula
        }
    
    @staticmethod
    def list_all():
        configuracao = Configuracao.query.all()
        resultado = [{
            "Id": c.id_configuracao,
            "Status": c.status,
            "Alunos Ausentes": c.aluno_ausente,
            "Inicio Aula": c.inicio_aula,
            "Final Aula": c.final_aula  
          }for c in configuracao]
        
        return jsonify(resultado)
    
    @staticmethod
    def update (id, data):
        configuracao = Configuracao.query.get(id)

        configuracao.status = data.status
        configuracao.aluno_ausente = data.aluno_ausente
        configuracao.inicio_aula = data.inicio_aula
        configuracao.final_aula = data.final_aula

        MainRepository.db.session.merge(configuracao)
        MainRepository.db.session.commit()
        return {"mensagem":"sucesso"}
    
    @staticmethod
    def delete (id):
        configuracao = Configuracao.query.get(id)
        
        configuracao.ativo= False
        
        MainRepository.db.session.merge(configuracao)
        MainRepository.db.session.commit()
        
        return {"mensagem":"sucesso"}

    @staticmethod
    def register(configuracao):

        MainRepository.db.session.add(configuracao)
        MainRepository.db.session.commit()

        return "Configuracao criada com sucesso"