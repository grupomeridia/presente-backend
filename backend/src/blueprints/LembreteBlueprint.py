from flask import Blueprint, request, jsonify
from datetime import datetime
from repository.LembreteRepository import LembreteRepository

from dtos.LembreteDTO import LembreteDTO

from service.LembreteService import LembreteService

lembretes = Blueprint("lembretes", __name__)

@lembretes.route("/api/lembrete", methods=['GET', 'POST', 'PUT', 'DELETE'])
def lembrete():
    if request.method == 'GET':
        id_lembrete = request.args.get('id')
        try:
            return jsonify(LembreteService.get_by_id(id_lembrete))
        except AssertionError as error:
            return str(error), 400
    
    if request.method == 'POST':
        data = request.json

        criacao = datetime.now()
        visualizacao = None
        status = True
        id_secretaria = data.get('id_secretaria', 'NOT_FOUND')
        destinatario_cargo = data.get('destinatario_cargo', 'NOT_FOUND')
        destinatario_id = data.get('destinatario_id', 'NOT_FOUND')
        titulo = data.get('titulo', 'NOT_FOUND')
        mensagem = data.get('mensagem', 'NOT_FOUND')
        

        try:
            return LembreteService.register(criacao, status, id_secretaria,  destinatario_cargo, destinatario_id, titulo, mensagem)
        except AssertionError as error:
            return str(error), 400
    
    if request.method == 'PUT':
        id_lembrete = request.args.get('id')
        data = request.json
        
        status = True
        id_secretaria = data.get('id_secretaria', 'NOT_FOUND')
        destinatario_cargo = data.get('destinatario_cargo', 'NOT_FOUND')
        destinatario_id = data.get('destinatario_id', 'NOT_FOUND')
        titulo = data.get('titulo', 'NOT_FOUND')
        mensagem = data.get('mensagem', 'NOT_FOUND')
        visualizacao = data.get('visualizacao', 'NOT_FOUND')
        
        try:
            return LembreteService.update(id_lembrete, id_secretaria, status, destinatario_cargo, destinatario_id, titulo, mensagem, criacao, visualizacao)
        except AssertionError as error:
            return str(error), 400
    
    if request.method == 'DELETE':
        id_lembrete = request.args.get('id')
        try:
            return jsonify(LembreteService.delete(id_lembrete))
        except AssertionError as error:
            return str(error), 400
    
@lembretes.route("/api/lembrete/listAll", methods=['GET'])
def list_all():
    return LembreteRepository.list_all()