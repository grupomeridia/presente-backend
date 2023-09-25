from flask import Blueprint, request, jsonify

from repository.ConfiguracaoRepository import ConfiguracaoRepository
from repository.MainRepository import MainRepository
from dtos.ConfiguracaoDTO import ConfiguracaoDTO
from entity.Configuracao import Configuracao

from service.ConfiguracaoService import ConfiguracaoService

configuracoes = Blueprint("configuracoes", __name__)

@configuracoes.route("/api/configuracao", methods=['GET', 'POST', 'PUT', 'DELETE'])
def configuracao():
    if request.method == 'GET':
        id = request.args.get('id')
        try:
            return jsonify(ConfiguracaoService.getConfiguracaoById(id))
        except AssertionError as error:
            return str(error)
    
    if request.method == 'POST':
        data = request.json

        status = True
        alunoAusente = data['alunoAusente']
        inicioAula = data['inicioAula']
        finalAula = data['finalAula']

        try:
            return ConfiguracaoService.register(ConfiguracaoDTO(status, alunoAusente, inicioAula, finalAula))
        except AssertionError as error:
            return str(error)
            
    if request.method == 'PUT':
        id = request.args.get('id')
        data = request.json

        status = True
        alunoAusente = data['alunoAusente']
        inicioAula = data['inicioAula']
        finalAula = data['finalAula']

        
        return jsonify(ConfiguracaoService.update(id, ConfiguracaoDTO))
    
    if request.method == 'DELETE':
        id = request.args.get('id')
        return jsonify(ConfiguracaoService.delete(id))


