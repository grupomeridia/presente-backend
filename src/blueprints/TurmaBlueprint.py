from flask import Blueprint, request, jsonify

from repository.MainRepository import MainRepository
from repository.TurmaRepository import TurmaRepository

from entity.Turma import Turma

turmas = Blueprint("turmas", __name__)

@turmas.route("/api/turma", methods=['GET', 'POST', 'PUT', 'DELETE'])
def turma():
    if request.method == 'GET':
        id = request.args.get('id')
        return jsonify(TurmaRepository.getTurmaById(id))

    if request.method == 'POST':
        data = request.json

        ativo = data['ativo']
        nome = data['nome']
        ano = data['ano']
        semestre = data['semestre']

        MainRepository.db.session.add(Turma(ativo, nome, ano, semestre))
        MainRepository.db.session.commit()

        return "Turma Cadastrada!"

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