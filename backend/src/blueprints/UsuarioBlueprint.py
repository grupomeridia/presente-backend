from flask import Blueprint, request, jsonify

from repository.UsuarioRepository import UsuarioRepository

from entity.Usuario import Usuario
from dtos.UsuarioDTO import UsuarioDTO
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
            return str(error)
        
    if request.method == 'POST':
        data = request.json
                
        status = True
        login = data.get('login', 'NOT_FOUND')
        senha = data.get('senha', 'NOT_FOUND')
        cargo = data.get('cargo', 'NOT_FOUND')

        if not cargo or cargo not in [cargo.value for cargo in Cargo]:
            return jsonify({"error": "Campo 'cargo' inválido."}), 400

        try:
            return UsuarioService.register(UsuarioDTO(status=status, login=login, senha=senha, cargo=cargo))
        except AssertionError as error:
            return str(error)
        
    if request.method == 'PUT':
        id_usuario = request.args.get('id')
        data = request.json

        status = True
        login = data['login']
        senha = data['senha']
        cargo = data['cargo']

        return UsuarioService.update(id_usuario, UsuarioDTO(status=status, login=login, senha=senha, cargo=cargo))
    
    if request.method == 'DELETE':
        id_usuario = request.args.get('id')
        try:
            return jsonify(UsuarioService.delete(id_usuario))
        except AssertionError as error:
            return str(error)