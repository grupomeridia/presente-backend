from flask import jsonify
from repository.MainRepository import MainRepository

from entity.Configuracao import Configuracao

class ConfiguracaoRepository():
    def getConfiguracaoById(id):
        return{
            "id": Configuracao.query.get(id).id,
            "Ativo": Configuracao.get(id).ativo,
            "Turma_Id": Configuracao.get(id).turma_id,
            "Projeto_Id": Configuracao.get(id).prjeto_id
        }
    def listAll():
        configuracao = Configuracao.query.all()
        resultado = [{
            "Id": a.id,
            "Ativo": a.ativo,
            "Turma_Id": a.turma_id,
            "Projeto_Id": a.prjeto_id  
          }for a in configuracao]
        return jsonify(resultado)
    
    def update (id, data):
        configuracao = Configuracao.query.get(id)

        configuracao.ativo = data ['ativo']
        configuracao.turma_id = data ['turma_id']
        configuracao.projeto_id = data['projeto_id']

        MainRepository.db.session.merge(configuracao)
        MainRepository.db.session.commit()
        return {"mensagem":"sucesso"}
    
    def delete (id):
        configuracao = Configuracao.query.get(id)
        configuracao.ativo= False
        MainRepository.db.session.merge(configuracao)
        MainRepository.db.session.commit()
        return {"mensagem":"sucesso"}
