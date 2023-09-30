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
            return str(error)
    
    if request.method == 'POST':
        data = request.json
        
        id_secretaria = data['id_secretaria']
        destinatario_cargo = data['destinatario_cargo']
        destinatario_id = data['destinatario_id']
        titulo = data['titulo']
        mensagem = data['mensagem']
        criacao = datetime.now()
        visualizacao = None
        
        try:
            return LembreteService.register(LembreteDTO(id_secretaria=id_secretaria, destinatario_cargo=destinatario_cargo, destinatario_id=destinatario_id, titulo=titulo, mensagem=mensagem, criacao=criacao, visualizacao=visualizacao))
        except AssertionError as error:
            return str(error)
    
    if request.method == 'PUT':
        id_lembrete = request.args.get('id')
        data = request.json
        
        id_secretaria = data['idSecretaria']
        destinatario_cargo = data['destinatario_cargo']
        destinatario_id = data['destinatorio_id']
        titulo = data['titulo']
        mensagem = data['mensagem']
        criacao = data['criacao']
        visualizacao = data['visualizacao']
        
        try:
            return LembreteService.update(id_lembrete, LembreteDTO(id_secretaria=id_secretaria, destinatario_cargo=destinatario_cargo, destinatario_id=destinatario_id, titulo=titulo, mensagem=mensagem, criacao=criacao, visualizacao=visualizacao))
        except AssertionError as error:
            return str(error)
    
    if request.method == 'DELETE':
        id_lembrete = request.args.get('id')
        try:
            return jsonify(LembreteService.delete(id_lembrete))
        except AssertionError as error:
            return str(error)
    
@lembretes.route("/api/lembrete/listAll", methods=['GET'])
def list_all():
    return LembreteRepository.list_all()