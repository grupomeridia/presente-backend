from flask import Blueprint, request, jsonify
from datetime import datetime
from repository.MainRepository import MainRepository
from repository.ChamadaRepository import ChamadaRepository
from dtos.ChamadaDTO import ChamadaDTO
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

        id_materia = data['idMateria']
        id_turma = data['idTurma']
        id_professor = data['idProfessor']
        status = True
        abertura = datetime.now()
        
        try:
            return ChamadaService.register(ChamadaDTO(id_materia=id_materia, id_turma=id_turma, id_professor=id_professor, status=status, abertura=abertura))
        except AssertionError as error:
            return str(error)

    if request.method == 'PUT':
        id = request.args.get('id')
        data = request.json

        id_materia = data['idMateria']
        id_turma = data['idTurma']
        id_professor = data['idProfessor']
        status = True
        abertura = data['abertura']
        encerramento = data['encerramento']
        try:
            return ChamadaService.update(id, ChamadaDTO(id_materia=id_materia, id_turma=id_turma, id_professor=id_professor, status=status, abertura=abertura, encerramento=encerramento))
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