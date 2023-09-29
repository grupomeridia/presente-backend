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

        id_configuracao = data['id_configuracao']
        id_secretaria = data['id_secretaria']
        date_criado = data['data_criado']
        total_ativos = data['total_ativos']
        total_presentes = data['total_presentes']
        total_ausentes = data['total_ausentes']
        total_presentes_curso = data['total_presentes_curso']
        total_ativo_curso = data['total_ativo_curso']
        total_ausente_curso = data['total_ausente_curso']

        try:
            return PainelService.register(PainelDTO(id_configuracao=id_configuracao, id_secretaria=id_secretaria, data_criado=date_criado, total_ativos=total_ativos, total_ausentes=total_ausentes, total_presentes=total_presentes, total_presentes_curso=total_presentes_curso, total_ativo_curso=total_ativo_curso, total_ausente_curso=total_ausente_curso))
        except AssertionError as error:
            return str(error)
    
    if request.method == 'PUT':
        id = request.args.get('id')
        data = request.json

        id_configuracao = data['id_configuracao']
        id_secretaria = data['id_secretaria']
        date_criado = data['data_criado']
        total_ativos = data['total_ativos']
        total_presentes = data['total_presentes']
        total_ausentes = data['total_ausentes']
        total_presentes_curso = data['total_presentes_curso']
        total_ativo_curso = data['total_ativo_curso']
        total_ausente_curso = data['total_ausente_curso']

        try:
            return PainelService.update(id, PainelDTO(id_configuracao=id_configuracao, id_secretaria=id_secretaria, data_criado=date_criado, total_ativos=total_ativos, total_ausentes=total_ausentes, total_presentes=total_presentes, total_presentes_curso=total_presentes_curso, total_ativo_curso=total_ativo_curso, total_ausente_curso=total_ausente_curso))
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