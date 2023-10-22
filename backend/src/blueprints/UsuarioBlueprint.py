from flask import Blueprint, request, jsonify, redirect, url_for

from repository.UsuarioRepository import UsuarioRepository

from entity.Usuario import Usuario
from entity.CargoEnum import Cargo

from service.UsuarioService import UsuarioService

usuarios = Blueprint("usuario", __name__)

@usuarios.route("/api/usuario", methods=['GET', 'POST', 'PUT', 'DELETE'])
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
        cargo = data.get('cargo', 'NOT_FOUND')

        try:
            return UsuarioService.register(status=status, login=login, senha=senha, cargo=cargo)
        except AssertionError as error:
            return str(error), 400
        
    if request.method == 'PUT':
        id_usuario = request.args.get('id')
        data = request.json

        status = True
        login = data.get('login', 'NOT_FOUND')
        senha = data.get('senha', 'NOT_FOUND')
        cargo = data.get('cargo', 'NOT_FOUND')

        return UsuarioService.update(id_usuario=id_usuario, status=status, login=login, senha=senha, cargo=cargo)

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

@usuarios.route("/api/register", methods=['POST'])
def register():
    pass
        
