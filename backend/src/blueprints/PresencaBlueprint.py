from flask import Blueprint, request, jsonify
from datetime import datetime

from repository.PresencaRepository import PresencaRepository

from entity.Presenca import Presenca
from dtos.PresencaDTO import PresencaDTO

from service.PresencaService import PresencaService

presencas = Blueprint("presencas", __name__)

@presencas.route("/api/presenca", methods=['GET', 'POST', 'PUT', 'DELETE'])
def presencas_main():
    if request.method == 'GET':
        id_presenca = request.args.get('id')
        try:
            return jsonify(PresencaService.get_by_id(id_presenca))
        except AssertionError as error:
            return str(error), 400
    
    if request.method == 'POST':
        data = request.json

        status = True
        id_aluno = data.get('id_aluno', 'NOT_FOUND')
        id_chamada = data.get('id_chamada', 'NOT_FOUND')
        tipo_presenca = data.get('tipo_presenca', 'NOT_FOUND')
        horario = data.get('horario', 'NOT_FOUND')

        try:
            return PresencaService.register(id_aluno=id_aluno, id_chamada=id_chamada, status=status, tipo_presenca=tipo_presenca, horario=horario)
        except AssertionError as error:
            return str(error), 400
    
    if request.method == 'PUT':
        id_presenca = request.args.get('id')
        data = request.json

        status = True
        id_aluno = data.get('id_aluno', 'NOT_FOUND')
        id_chamada = data.get('id_chamada', 'NOT_FOUND')
        tipo_presenca = data.get('tipo_presenca', 'NOT_FOUND')
        horario = data.get('horario', 'NOT_FOUND')

        try:
            return PresencaService.update(id_presenca=id_presenca, id_aluno=id_aluno, id_chamada=id_chamada, status=status, tipo_presenca=tipo_presenca, horario=horario)
        except AssertionError as error:
            return str(error), 400
        
    if request.method == 'DELETE':
        id_presenca = request.args.get('id')
        try:
            return jsonify(PresencaService.delete(id_presenca))
        except AssertionError as error:
            return str(error), 400

@presencas.route("/api/presenca/ra", methods=['POST'])
def marcar_presenca_pelo_ra():
    data = request.json

    ra = data.get('ra')
    cargo_manual = data.get('cargo_manual')
    id_manual = data.get('id_manual')

    try:
        return PresencaService.marcar_presenca_pelo_ra(ra, cargo_manual, id_manual)
    except AssertionError as error:
        return str(error), 400

@presencas.route("/api/presenca/listAll", methods=['GET'])
def list_all():
    return PresencaRepository.list_all()

@presencas.route("/api/presenca/findByPresentes", methods=['GET'])
def find_by_presentes():
    return PresencaRepository.find_by_presentes()