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
            return LembreteService.register(criacao=criacao, status=status, id_secretaria=id_secretaria,  destinatario_cargo=destinatario_cargo, destinatario_id=destinatario_id, titulo=titulo, mensagem=mensagem)
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
        visualizacao = data.get('visualizacao', None)
        criacao = data.get('criacao', None)
        
        try:
            return LembreteService.update(id_lembrete=id_lembrete, id_secretaria=id_secretaria, status=status, destinatario_cargo=destinatario_cargo, destinatario_id=destinatario_id, titulo=titulo, mensagem=mensagem, visualizacao=visualizacao, criacao=criacao)
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
    return LembreteRepository.lista_all()

@lembretes.route("/api/lembrete/findLembrete", methods=['GET'])
def find_lembrete():
    cargo = request.args.get('cargo')
    id = request.args.get('id')
    try:
        return LembreteService.find_lembrete(cargo, id)
    except AssertionError as error:
        return str(error), 400
    
@lembretes.route("/api/lembrete/visualizar", methods=['PUT'])
def lembrete_visualizado():
    id_lembrete = request.args.get('id')
    try: 
        return LembreteService.lembrete_visualizado(id_lembrete)
    except AssertionError as error:
        return str(error), 400
    
@lembretes.route("/api/lembrete/visualizados", methods=['GET'])
def lembretes_visualizados():
    try:
        return LembreteRepository.lembretes_visualizados()
    except AssertionError as error:
        return str(error), 400
    