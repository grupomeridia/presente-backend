from flask import Blueprint, request, jsonify

from repository.PainelRepository import PainelRepository
from dtos.PainelDTO import PainelDTO
from service.PainelService import PainelService

paineis = Blueprint("painel", __name__)

@paineis.route("/api/painel", methods=['GET', 'POST', 'PUT', 'DELETE'])
def painel():
    if request.method == 'GET':
        id = request.args.get('id')
        try:
            return jsonify(PainelService.getById(id))
        except AssertionError as error:
            return str(error)
    
    if request.method == 'POST':
        data = request.json

        id_configuracao = data['idConfiguracao']
        id_secretaria = data['idSecretaria']
        date = data['data']
        totalAtivos = data['totalAtivos']
        totalPresentes = data['totalPresentes']
        totalAusentes = data['totalAusentes']
        totalPresentesCurso = data['totalPresentesCurso']
        totalAtivoCurso = data['totalAtivoCurso']
        totalAusenteCurso = data['totalAusenteCurso']

        try:
            return PainelService.register(PainelDTO(id_configuracao=id_configuracao, id_secretaria=id_secretaria, data=date, totalAtivos=totalAtivos, totalAusentes=totalPresentes, totalPresentesCurso=totalPresentesCurso, totalAtivoCurso=totalAtivoCurso, totalAusenteCurso=totalAusenteCurso))
        except AssertionError as error:
            return str(error)
    
    if request.method == 'PUT':
        id = request.args.get('id')
        data = request.json

        id_configuracao = data['idConfiguracao']
        id_secretaria = data['idSecretaria']
        date = data['data']
        totalAtivos = data['totalAtivos']
        totalPresentes = data['totalPresentes']
        totalAusentes = data['totalAusentes']
        totalPresentesCurso = data['totalPresentesCurso']
        totalAtivoCurso = data['totalAtivoCurso']
        totalAusenteCurso = data['totalAusenteCurso']

        try:
            return PainelService.update(id, PainelDTO(id_configuracao=id_configuracao, id_secretaria=id_secretaria, data=date, totalAtivos=totalAtivos, totalAusentes=totalPresentes, totalPresentesCurso=totalPresentesCurso, totalAtivoCurso=totalAtivoCurso, totalAusenteCurso=totalAusenteCurso))
        except AssertionError as error:
            return str(error)
        
    if request.method == 'DELETE':
        id = request.args.get('id')
        try:
            return jsonify(PainelService.delete(id))
        except AssertionError as error:
            return str(error)
    
@paineis.route("/api/painel/listAll", methods=['GET'])
def listAll():
    return PainelRepository.listAll()