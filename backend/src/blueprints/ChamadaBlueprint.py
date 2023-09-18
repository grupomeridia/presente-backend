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

        idMateria = data['idMateria']
        idTurma = data['idTurma']
        idProfessor = data['idProfessor']
        status = True
        abertura = data['abertura']
        encerramento = data['encerramento']
        
        try:
            return ChamadaService.register(idMateria, idTurma, idProfessor, status, abertura, encerramento)
        except AssertionError as error:
            return str(error)

    if request.method == 'PUT':
        id = request.args.get('id')
        data = request.json

        idMateria = data['idMateria']
        idTurma = data['idTurma']
        idProfessor = data['idProfessor']
        abertura = data['abertura']
        encerramento = data['encerramento']

        try:
            return jsonify(ChamadaService.update(id, idMateria, idTurma, idProfessor, status, abertura, encerramento))
        except AssertionError as error:
            return str(error)

    if request.method == 'DELETE':
        id = request.args.get('id')

        try:
            return jsonify(ChamadaService.delete(id))
        except AssertionError as error:
            return str(error)


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