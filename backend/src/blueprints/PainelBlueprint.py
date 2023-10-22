from flask import Blueprint, request, jsonify
from datetime import datetime
from repository.PainelRepository import PainelRepository
from dtos.PainelDTO import PainelDTO
from service.PainelService import PainelService

paineis = Blueprint("painel", __name__)

@paineis.route("/api/painel", methods=['GET', 'POST', 'PUT', 'DELETE'])
def painel():
    if request.method == 'GET':
        id_painel = request.args.get('id')
        try:
            return jsonify(PainelService.get_by_id(id_painel))
        except AssertionError as error:
            return str(error), 400
    
    if request.method == 'POST':
        data = request.json

        data_criado = datetime.now()
        status = True
        id_configuracao = data.get('id_configuracao', 'NOT_FOUND')
        id_secretaria = data.get('id_secretaria', 'NOT_FOUND')
        total_ativo = data.get('total_ativo', 'NOT_FOUND')
        total_presentes = data.get('total_presentes', 'NOT_FOUND')
        total_ausentes = data.get('total_ausentes', 'NOT_FOUND')
        total_presentes_curso = data.get('total_presentes_curso', 'NOT_FOUND')
        total_ativo_curso = data.get('total_ativo_curso', 'NOT_FOUND')
        total_ausente_curso = data.get('total_ausente_curso', 'NOT_FOUND')

        print(data)
        try:
            return PainelService.register(id_configuracao=id_configuracao, id_secretaria=id_secretaria, total_ativo=total_ativo, total_ausentes=total_ausentes, total_presentes=total_presentes, total_presentes_curso=total_presentes_curso, total_ativo_curso=total_ativo_curso, total_ausente_curso=total_ausente_curso, status=status, data_criado=data_criado)
        except AssertionError as error:
            return str(error), 400
    
    if request.method == 'PUT':
        id_painel = request.args.get('id')
        data = request.json

        data_criado = datetime.now()
        status = True
        id_configuracao = data.get('id_configuracao', 'NOT_FOUND')
        id_secretaria = data.get('id_secretaria', 'NOT_FOUND')
        total_ativo = data.get('total_ativo', 'NOT_FOUND')
        total_presentes = data.get('total_presentes', 'NOT_FOUND')
        total_ausentes = data.get('total_ausentes', 'NOT_FOUND')
        total_presentes_curso = data.get('total_presentes_curso', 'NOT_FOUND')
        total_ativo_curso = data.get('total_ativo_curso', 'NOT_FOUND')
        total_ausente_curso = data.get('total_ausente_curso', 'NOT_FOUND')

        try:
            return PainelService.update(id_painel=id_painel, id_configuracao=id_configuracao, id_secretaria=id_secretaria, total_ativo=total_ativo, total_ausentes=total_ausentes, total_presentes=total_presentes, total_presentes_curso=total_presentes_curso, total_ativo_curso=total_ativo_curso, total_ausente_curso=total_ausente_curso, status=status, data_criado=data_criado)
        except AssertionError as error:
            return str(error), 400
        
    if request.method == 'DELETE':
        id_painel = request.args.get('id')
        try:
            return jsonify(PainelService.delete(id_painel))
        except AssertionError as error:
            return str(error), 400
    
@paineis.route("/api/painel/listAll", methods=['GET'])
def list_all():
    return PainelRepository.list_all()