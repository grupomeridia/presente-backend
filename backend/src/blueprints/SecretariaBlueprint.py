from flask import Blueprint, request, jsonify

from repository.SecretariaRepository import SecretariaRepository

from dtos.SecretariaDTO import SecretariaDTO

from service.SecretariaService import SecretariaService

secretaria = Blueprint("secretaria", __name__)

@secretaria.route("/api/secretaria", methods=['GET', 'POST', 'PUT', 'DELETE'])
def secret():
    if request.method == 'GET':
        id = request.args.get('id')
        try:
            return jsonify(SecretariaService.getById(id))
        except AssertionError as error:
            return str(error)
        
    if request.method == 'POST':
        data = request.json
        
        id_usuario = data['idUsuario']
        status = True
        nome = data['nome']
        
        try:
            return SecretariaService.register(SecretariaDTO(id_usuario=id_usuario, status=status, nome=nome))
        except AssertionError as error:
            return str(error)
    
    if request.method == 'PUT':
        id = request.args.get('id')
        data = request.json
        
        id_usuario = data['idUsuario']
        status = True
        nome = data['nome']
        
        try:
            return SecretariaService.update(id, SecretariaDTO(id_usuario=id_usuario, status=status, nome=nome))
        except AssertionError as error:
            return str(error)
    
    if request.method == 'DELETE':
        id = request.args.get('id')
        try:
            return jsonify(SecretariaService.delete(id))
        except AssertionError as error:
            return str(error)

@secretaria.route("/api/secretaria/listAll", methods=['GET'])
def listAll():
    return SecretariaRepository.listAll()