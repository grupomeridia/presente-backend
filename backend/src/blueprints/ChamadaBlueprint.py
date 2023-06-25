from flask import Blueprint, request, jsonify

from repository.MainRepository import MainRepository
from repository.ChamadaRepository import ChamadaRepository

from entity.Chamada import Chamada

chamadas = Blueprint("chamadas", __name__)

@chamadas.route("/api/chamada", methods=['GET', 'POST', 'PUT', 'DELETE'])
def professor():
    if request.method == 'GET':
        id = request.args.get('id')
        return jsonify(ChamadaRepository.getChamadaById(id))
    
    if request.method == 'POST':
        data = request.json

        ativo = data['ativo']
        projeto = data['projeto']
        professor = data['professor']
        turma = data['turma']

        MainRepository.db.session.add(Chamada(ativo, projeto, professor, turma))
        MainRepository.db.session.commit()

        return "Chamada Cadastrada!"

    if request.method == 'PUT':
        id = request.args.get('id')
        data = request.json
        return jsonify(ChamadaRepository.update(id, data))
    
    if request.method == 'DELETE':
        id = request.args.get('id')
        return jsonify(ChamadaRepository.delete(id))

@chamadas.route("/api/chamada/listAll", methods=['GET'])
def listarAllChamadas():
    return ChamadaRepository.listAll()
