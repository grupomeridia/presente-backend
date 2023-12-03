from flask import Blueprint, request, jsonify
from repository.ChamadaRepository import ChamadaRepository
from flask_jwt_extended import jwt_required

from service.ChamadaService import ChamadaService

chamadas = Blueprint("chamadas", __name__)

@chamadas.route("/api/chamada", methods=['GET', 'POST', 'PUT', 'DELETE'])
@jwt_required()
def professor():
    if request.method == 'GET':
        id_chamada = request.args.get('id')
        try:
            return jsonify(ChamadaService.get_by_id(id_chamada))
        except AssertionError as error:
            return str(error), 400
    
    if request.method == 'POST':
        data = request.json

        status = data.get('status', 'NOT_FOUND')
        abertura = data.get('abertura', 'NOT_FOUND')
        encerramento = data.get('encerramento', 'NOT_FOUND')
        id_turma = data.get('id_turma', 'NOT_FOUND')
        id_professor = data.get('id_professor', 'NOT_FOUND')
        
        try:
            return ChamadaService.register(id_turma=id_turma,id_professor=id_professor, status=status, abertura=abertura, encerramento=encerramento)
        except AssertionError as error:
            return str(error), 400

    if request.method == 'PUT':
        id_chamada = request.args.get('id')
        data = request.json

        status =  data.get('status', 'NOT_FOUND')
        id_turma = data.get('id_turma', 'NOT_FOUND')
        id_professor = data.get('id_professor', 'NOT_FOUND')
        abertura = data.get('abertura', 'NOT_FOUND')
        encerramento = data.get('encerramento', 'NOT_FOUND')
        try:
            return ChamadaService.update(id_chamada=id_chamada, id_turma=id_turma, id_professor=id_professor, status=status, abertura=abertura, encerramento=encerramento)
        except AssertionError as error:
            return str(error), 400

    if request.method == 'DELETE':
        id_chamada = request.args.get('id')

        try:
            return jsonify(ChamadaService.delete(id_chamada))
        except AssertionError as error:
            return str(error), 400


@chamadas.route("/api/chamada/listAll", methods=['GET'])
@jwt_required()
def listar_all_chamadas():
    return ChamadaRepository.list_all()

@chamadas.route("/api/chamada/listAllprofessor", methods=['GET'])
@jwt_required()
def listar_all_chamadas_professor():
    id_professor = request.args.get('id')
    try:
        return jsonify(ChamadaService.listar_all_chamadas_professor(id_professor))
    except AssertionError as error:
        return str(error), 400

@chamadas.route("/api/chamada/aluno", methods=['GET'])
@jwt_required()
def chamadas_abertas():
    id_aluno = request.args.get('id')
    try: 
        return jsonify(ChamadaRepository.get_chamadas_abertas_aluno(id_aluno))
    except AssertionError as error:
        return str(error), 400
    
@chamadas.route("/api/chamada/fecharChamada", methods=['PUT'])
@jwt_required()
def fechar_chamada():
    id_chamada = request.args.get('id')
    try:
        return ChamadaService.fechar_chamada(id_chamada)
    except AssertionError as error:
        return str(error), 400
    
@chamadas.route("/api/chamada/updateAll", methods=['GET'])
@jwt_required()
def updateAll():
    try:
        return ChamadaRepository.update_all()
    except Exception as error:
        return str(error), 400
    
@chamadas.route("/api/chamada/ultimaChamada", methods=['GET'])
@jwt_required()
def ultimaChamada():
    id_professor = request.args.get('id')
    try:
        return jsonify(ChamadaRepository.ultimaChamada(id_professor))
    except AssertionError as error:
        return str(error), 400
    