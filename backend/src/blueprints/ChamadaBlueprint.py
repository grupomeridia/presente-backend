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
        id_chamada = request.args.get('id')
        try:
            return jsonify(ChamadaService.get_by_id(id_chamada))
        except AssertionError as error:
            return str(error)
    
    if request.method == 'POST':
        data = request.json

        id_materia = data['id_materia']
        id_turma = data['id_turma']
        id_professor = data['id_professor']
        status = True
        abertura = datetime.now()
        encerramento = None
        
        try:
            return ChamadaService.register(ChamadaDTO(id_materia=id_materia, id_turma=id_turma, id_professor=id_professor, status=status, abertura=abertura, encerramento=encerramento))
        except AssertionError as error:
            return str(error)

    if request.method == 'PUT':
        id_chamada = request.args.get('id')
        data = request.json

        id_materia = data['id_materia']
        id_turma = data['id_turma']
        id_professor = data['id_professor']
        status = True
        abertura = data['abertura']
        encerramento = data['encerramento']
        try:
            return ChamadaService.update(id_chamada, ChamadaDTO(id_materia=id_materia, id_turma=id_turma, id_professor=id_professor, status=status, abertura=abertura, encerramento=encerramento))
        except AssertionError as error:
            return str(error)

    if request.method == 'DELETE':
        id_chamada = request.args.get('id')

        try:
            return jsonify(ChamadaService.delete(id_chamada))
        except AssertionError as error:
            return str(error)


@chamadas.route("/api/chamada/listAll", methods=['GET'])
def listar_all_chamadas():
    return ChamadaRepository.listAll()


@chamadas.route("/api/chamada/aluno", methods=['GET'])
def chamadas_abertas():
    id_chamada = request.args.get('id')
    try: 
        return jsonify(ChamadaRepository.get_chamadas_abertas_aluno(id_chamada))
    except AssertionError as error:
        return str(error)