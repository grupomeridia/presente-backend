from flask import Blueprint, request, jsonify

from repository.MainRepository import MainRepository
from repository.ProjetoRepository import ProjetoRepository

from entity.Projeto import Projeto

projetos = Blueprint("projetos", __name__)   

@projetos.route("/api/projeto", methods=['GET', 'POST','PUT','DELETE'])
def projeto():
    if request.method == 'GET':
        id = request.args.get('id')
        return jsonify(ProjetoRepository.getProjetoById(id))
    
    if request.method == 'POST':
        data = request.json
    
        ativo = data['ativo']
        nome = data['nome']

        MainRepository.db.session.add(Projeto(ativo, nome))
        MainRepository.db.session.commit()

        return "Projeto Cadastrado!"
    
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