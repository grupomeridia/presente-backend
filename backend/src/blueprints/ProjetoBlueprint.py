from flask import Blueprint, request, jsonify

from repository.MainRepository import MainRepository
from repository.ProjetoRepository import ProjetoRepository

from entity.Projeto import Projeto

from service.ProjetoService import ProjetoService

projetos = Blueprint("projetos", __name__)   

@projetos.route("/api/projeto", methods=['GET', 'POST','PUT','DELETE'])
def projeto():
    if request.method == 'GET':
        id = request.args.get('id')
        try:    
            return jsonify(ProjetoService.getProjeto(id))
        except AssertionError as error:
            return str(error)
    
    if request.method == 'POST':
        data = request.json
    
        ativo = data['ativo']
        nome = data['nome']

        try:
            return ProjetoService.postProjeto(ativo, nome)
        except AssertionError as error:
            return str(error)
    
    if request.method == 'PUT':
        id = request.args.get('id')
        data = request.json    
        return jsonify(ProjetoRepository.update(id, data))
    
    if request.method == 'DELETE':
        id = request.args.get('id')
        return jsonify(ProjetoRepository.delete(id))

    
@projetos.route("/api/projeto/listAll", methods=['GET'])
def listarAllProjetos():
    return ProjetoRepository.listAll()