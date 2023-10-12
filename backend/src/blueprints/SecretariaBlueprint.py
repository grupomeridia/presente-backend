from flask import Blueprint, request, jsonify

from repository.SecretariaRepository import SecretariaRepository

from dtos.SecretariaDTO import SecretariaDTO

from service.SecretariaService import SecretariaService

secretaria = Blueprint("secretaria", __name__)

@secretaria.route("/api/secretaria", methods=['GET', 'POST', 'PUT', 'DELETE'])
def secret():
    if request.method == 'GET':
        id_secretaria = request.args.get('id')
        try:
            return jsonify(SecretariaService.get_by_id(id_secretaria))
        except AssertionError as error:
            return str(error), 400
        
    if request.method == 'POST':
        data = request.json
        
        status = True
        id_usuario = data.get('id_usuario', 'NOT_FOUND')
        nome = data.get('nome', 'NOT_FOUND')
        
        try:
            return SecretariaService.register(id_usuario=id_usuario, status=status, nome=nome)
        except AssertionError as error:
            return str(error), 400
    
    if request.method == 'PUT':
        id_secretaria = request.args.get('id')
        data = request.json
        
        status = True
        id_secretaria = data.get('id_secretaria', 'NOT_FOUND')
        nome = data.get('nome', 'NOT_FOUND')
        
        try:
            return SecretariaService.update(id_secretaria=id_secretaria, status=status, nome=nome)
        except AssertionError as error:
            return str(error), 400
    
    if request.method == 'DELETE':
        id_secretaria = request.args.get('id')
        try:
            return jsonify(SecretariaService.delete(id_secretaria))
        except AssertionError as error:
            return str(error), 400 

@secretaria.route("/api/secretaria/listAll", methods=['GET'])
def list_all():
    return SecretariaRepository.list_all()