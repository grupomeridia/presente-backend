from flask import Blueprint, request, jsonify

from dtos.ConfiguracaoDTO import ConfiguracaoDTO

from service.ConfiguracaoService import ConfiguracaoService

configuracoes = Blueprint("configuracoes", __name__)

@configuracoes.route("/api/configuracao", methods=['GET', 'POST', 'PUT', 'DELETE'])
def configuracao():
    if request.method == 'GET':
        id_configuracao = request.args.get('id')
        try:
            return jsonify(ConfiguracaoService.get_configuracao_by_id(id_configuracao))
        except AssertionError as error:
            return str(error)
    
    if request.method == 'POST':
        data = request.json

        status = True
        aluno_ausente = data['aluno_ausente']
        inicio_aula = data['inicio_aula']
        fim_aula = data['fim_aula']

        try:
            return ConfiguracaoService.register(ConfiguracaoDTO(status=status, aluno_ausente=aluno_ausente, inicio_aula=inicio_aula, fim_aula=fim_aula))
        except AssertionError as error:
            return str(error)
            
    if request.method == 'PUT':
        id_configuracao = request.args.get('id')
        data = request.json

        status = True
        aluno_ausente = data['aluno_ausente']
        inicio_aula = data['inicio_aula']
        fim_aula = data['fim_aula']

        
        return ConfiguracaoService.update(id_configuracao, ConfiguracaoDTO(status=status, aluno_ausente=aluno_ausente, inicio_aula=inicio_aula, fim_aula=fim_aula))
    
    if request.method == 'DELETE':
        id_configuracao = request.args.get('id')
        return jsonify(ConfiguracaoService.delete(id_configuracao))


