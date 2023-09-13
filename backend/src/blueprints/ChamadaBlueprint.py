from flask import Blueprint, request, jsonify

from repository.MainRepository import MainRepository
from repository.ChamadaRepository import ChamadaRepository

from entity.Chamada import Chamada

from service.ChamadaService import ChamadaService

chamadas = Blueprint("chamadas", __name__)

@chamadas.route("/api/chamada", methods=['GET', 'POST', 'PUT', 'DELETE'])
def professor():
    if request.method == 'GET':
        id = request.args.get('id')
        try:
            return jsonify(ChamadaService.getById(id))
        except AssertionError as error:
            return str(error)
    
    if request.method == 'POST':
        data = request.json

        ativo = data['ativo']
        projeto_id = data['projeto_id']
        professor_id = data['professor_id']
        turma_id = data['turma_id']

        try:
            return ChamadaService.register(ativo, projeto_id, professor_id, turma_id)
        except AssertionError as error:
            return str(error)

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


@chamadas.route("/api/chamada/aluno", methods=['GET'])
def chamadasAbertas():
    id = request.args.get('id')
    try: 
        return jsonify(ChamadaService.chamadasAbertasAluno(id))
    except AssertionError as error:
        return str(error)