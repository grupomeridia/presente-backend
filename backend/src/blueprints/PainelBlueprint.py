from flask import Blueprint, request, jsonify

from repository.PainelRepository import PainelRepository
from dtos.PainelDTO import PainelDTO
from service.PainelService import PainelService

painel = Blueprint("painel", __name__)

@painel.route("/api/painel", methods=['GET', 'POST', 'PUT', 'DELETE'])
def painel():
    if request.method == 'GET':
        id = request.args.get('id')
        try:
            return jsonify(PainelService.getById(id))
        except AssertionError as error:
            return str(error)
    
    if request.method == 'POST':
        data = request.json

        date = data['data']
        totalAtivos = data['totalAtivos']
        totalPresentes = data['totalPresentes']
        totalAusentes = data['totalAusentes']
        totalPresentesCurso = data['totalPresentesCurso']
        totalAtivoCurso = data['totalAtivoCurso']
        totalAusenteCurso = data['totalAusenteCurso']

        try:
            return PainelService.register(PainelDTO(date, totalAtivos, totalPresentes, totalAusentes, totalPresentesCurso, totalAtivoCurso, totalAusenteCurso))
        except AssertionError as error:
            return str(error)
    
    if request.method == 'PUT':
        id = request.args.get('id')
        data = request.json

        date = data['data']
        totalAtivos = data['totalAtivos']
        totalPresentes = data['totalPresentes']
        totalAusentes = data['totalAusentes']
        totalPresentesCurso = data['totalPresentesCurso']
        totalAtivoCurso = data['totalAtivoCurso']
        totalAusenteCurso = data['totalAusenteCurso']

        try:
            return jsonify(PainelService.update(id, PainelDTO))
        except AssertionError as error:
            return str(error)
        
    if request.method == 'DELETE':
        id = request.args.get('id')
        try:
            return jsonify(PainelService.delete(id))
        except AssertionError as error:
            return str(error)
    
@painel.route("/api/painel/listAll", methods=['GET'])
def listAll():
    return PainelRepository.listAll()