from flask import Blueprint, request, jsonify

from repository.ConfiguracaoRepository import ConfiguracaoRepository
from repository.MainRepository import MainRepository

from entity.Configuracao import Configuracao

configuracoes = Blueprint("configuracoes", __name__)

@configuracoes.route("/api/configuracao", methods=['GET', 'POST', 'PUT', 'DELETE'])
def configuracao():
    if request.method == 'GET':
        id = request.args.get('id')
        return jsonify(ConfiguracaoRepository.getConfiguracaoById(id))
    
    if request.method == 'POST':
        data = request.json

        ativo = True
        turma_id = data['turmaId']
        projeto_id = data['projetoId']

        MainRepository.db.session.add(Configuracao(ativo, turma_id, projeto_id))
        MainRepository.db.session.commit()

        return {"mensagem":"sucesso"}
    
    if request.method == 'PUT':
        id = request.args.get('id')
        data = request.json
        
        return ConfiguracaoRepository.update(id, data)
    
    if request.method == 'DELETE':
        id = request.args.get('id')
        return ConfiguracaoRepository.delete(id)


