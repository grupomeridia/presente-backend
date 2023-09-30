from flask import Blueprint, request, jsonify
from datetime import datetime
from repository.MainRepository import MainRepository
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
            return str(error)
    
    if request.method == 'POST':
        data = request.json

        id_aluno = data['idAluno']
        id_chamada = data['idChamada']
        status = True
        tipo_presenca = data['tipoPresenca']
        horario = datetime.now()

        try:
            return PresencaService.register(PresencaDTO(id_aluno=id_aluno, id_chamada=id_chamada, status=status, tipoPresenca=tipo_presenca, horario=horario))
        except AssertionError as error:
            return str(error)
    
    if request.method == 'PUT':
        id_presenca = request.args.get('id')
        data = request.json

        id_aluno = data['idAluno']
        id_chamada = data['idChamada']
        status = True
        tipo_presenca = data['tipoPresenca']
        horario = data['horario']

        return PresencaService.update(id_presenca, PresencaDTO(id_aluno=id_aluno, id_chamada=id_chamada, status=status, tipoPresenca=tipo_presenca, horario=horario))
    
    if request.method == 'DELETE':
        id_presenca = request.args.get('id')
        return PresencaService.delete(id_presenca)

@presencas.route("/api/presenca/listAll", methods=['GET'])
def list_all():
    return PresencaRepository.list_all()

@presencas.route("/api/presenca/findByPresentes", methods=['GET'])
def find_by_presentes():
    return PresencaRepository.find_by_presentes()