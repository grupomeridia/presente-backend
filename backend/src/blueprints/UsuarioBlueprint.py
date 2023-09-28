from flask import Blueprint, request, jsonify

from repository.UsuarioRepository import UsuarioRepository
from repository.MainRepository import MainRepository

from entity.Usuario import Usuario
from dtos.UsuarioDTO import UsuarioDTO

from service.UsuarioService import UsuarioService

usuarios = Blueprint("usuario", __name__)

@usuarios.route("/api/usuario", methods=['GET', 'POST', 'PUT', 'DELETE'])
def usuario():
    if request.method == 'GET':
        id = request.args.get('id')
        try:
            return jsonify(UsuarioService.getUsuarioById(id))
        except AssertionError as error:
            return str(error)
        
    if request.method == 'POST':
        data = request.json
        
        status = True
        login = data['login']
        senha = data['senha']
        cargo = data['cargo']

        try:
            return UsuarioService.register(UsuarioDTO(status, login, senha, cargo))
        except AssertionError as error:
            return str(error)
        
    if request.method == 'PUT':
        id = request.args.get('id')
        data = request.json

        status = True
        login = data['login']
        senha = data['senha']
        cargo = data['cargo']

        return UsuarioService.update(id, UsuarioDTO(status, login, senha, cargo))
    
    if request.method == 'DELETE':
        id = request.args.get('id')
        return jsonify(UsuarioService.delete(id))