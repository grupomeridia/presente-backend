from flask import Blueprint, request, jsonify

from flask_jwt_extended import jwt_required

from service.UsuarioService import UsuarioService

usuarios = Blueprint("usuario", __name__)

@usuarios.route("/api/usuario", methods=['GET', 'POST', 'PUT', 'DELETE'])
@jwt_required()
def usuario():
    if request.method == 'GET':
        id_usuario = request.args.get('id')
        try:
            return jsonify(UsuarioService.get_usuario_by_id(id_usuario))
        except AssertionError as error:
            return str(error), 400
        
    if request.method == 'POST':
        data = request.json
                
        status = True
        login = data.get('login', 'NOT_FOUND')
        senha = data.get('senha', 'NOT_FOUND')
        nome = data.get('nome', 'NOT_FOUND')
        ra = data.get('ra', 'NOT_FOUND')
        cargo = data.get('cargo', 'NOT_FOUND')

        try:
            return UsuarioService.register(status=status, login=login, senha=senha, nome=nome, ra=ra, cargo=cargo)
        except AssertionError as error:
            return str(error), 400
        
    if request.method == 'PUT':
        id_usuario = request.args.get('id')
        data = request.json

        status = True
        login = data.get('login', 'NOT_FOUND')
        senha = data.get('senha', 'NOT_FOUND')
        nome = data.get('nome', 'NOT_FOUND')
        ra = data.get('ra', 'NOT_FOUND')
        cargo = data.get('cargo', 'NOT_FOUND')

        try:
            return UsuarioService.update(id_usuario=id_usuario, status=status, login=login, senha=senha, nome=nome, ra=ra, cargo=cargo)
        except AssertionError as error:
            return str(error), 400

    if request.method == 'DELETE':
        id_usuario = request.args.get('id')
        try:
            return jsonify(UsuarioService.delete(id_usuario))
        except AssertionError as error:
            return str(error), 400
        
@usuarios.route("/api/login", methods=['POST'])
def login():
    if request.method == 'POST':

        data = request.json

        login = data.get('login', 'NOT_FOUND')
        senha = data.get('senha', 'NOT_FOUND')

        try:
            return UsuarioService.login(login=login, senha=senha)
             
        except AssertionError as error:
            return str(error),400

