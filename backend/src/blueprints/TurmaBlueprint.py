from flask import Blueprint, request, jsonify

from repository.MainRepository import MainRepository
from repository.TurmaRepository import TurmaRepository

from entity.Turma import Turma

from service.TurmaService import TurmaService

turmas = Blueprint("turmas", __name__)

@turmas.route("/api/turma", methods=['GET', 'POST', 'PUT', 'DELETE'])
def turma():
    if request.method == 'GET':
        id = request.args.get('id')
        try:
            return jsonify(TurmaService.getTurma(id))
        except AssertionError as error:
            return str(error)

    if request.method == 'POST':
        data = request.json

        ativo = data['ativo']
        nome = data['nome']
        ano = data['ano']
        semestre = data['semestre']

        try:
            return TurmaService.postTurma(ativo, nome, ano, semestre)
        except AssertionError as error:
            return str(error)

        

    if request.method == 'PUT':
        id = request.args.get('id')
        data = request.json
        return jsonify(TurmaRepository.update(id, data))
    
    if request.method == 'DELETE':
        id = request.args.get('id')
        return jsonify(TurmaRepository.delete(id))

@turmas.route("/api/turma/listAll", methods=['GET'])
def listarAllTurmas():
    return TurmaRepository.listAll()