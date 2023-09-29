from flask import Blueprint, request, jsonify

from repository.LembreteRepository import LembreteRepository

from dtos.LembreteDTO import LembreteDTO

from service.LembreteService import LembreteService

lembretes = Blueprint("lembretes", __name__)

@lembretes.route("/api/lembrete", methods=['GET', 'POST', 'PUT', 'DELETE'])
def lembrete():
    if request.method == 'GET':
        id = request.args.get('id')
        try:
            return jsonify(LembreteService.getById(id))
        except AssertionError as error:
            return str(error)
    
    if request.method == 'POST':
        data = request.json
        
        id_secretaria = data['id_secretaria']
        destinatario_cargo = data['destinatario_cargo']
        destinatario_id = data['destinatario_id']
        titulo = data['titulo']
        mensagem = data['mensagem']
        criacao = data['criacao']
        visualizacao = data['visualizacao']
        
        try:
            return LembreteService.register(LembreteDTO(id_secretaria=id_secretaria, destinatario_cargo=destinatario_cargo, destinatario_id=destinatario_id, titulo=titulo, mensagem=mensagem, criacao=criacao, visualizacao=visualizacao))
        except AssertionError as error:
            return str(error)
    
    if request.method == 'PUT':
        id = request.args.get('id')
        data = request.json
        
        id_secretaria = data['idSecretaria']
        destinatario_cargo = data['destinatario_cargo']
        destinatario_id = data['destinatorio_id']
        titulo = data['titulo']
        mensagem = data['mensagem']
        criacao = data['criacao']
        visualizacao = data['visualizacao']
        
        try:
            return LembreteService.update(LembreteDTO(id_secretaria=id_secretaria, destinatario_cargo=destinatario_cargo, destinatario_id=destinatario_id, titulo=titulo, mensagem=mensagem, criacao=criacao, visualizacao=visualizacao))
        except AssertionError as error:
            return str(error)
    
    if request.method == 'DELETE':
        id = request.args.get('id')
        try:
            return jsonify(LembreteService.delete(id))
        except AssertionError as error:
            return str(error)
    
@lembretes.route("/api/lembrete/listAll", methods=['GET'])
def listAll():
    return LembreteRepository.listaAll()