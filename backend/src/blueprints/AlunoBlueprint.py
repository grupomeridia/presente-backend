from flask import Blueprint, request, jsonify

from repository.MainRepository import MainRepository
from repository.AlunoRepository import AlunoRepository

from entity.Aluno import Aluno

from service.AlunoService import AlunoService

alunos = Blueprint("alunos", __name__)

@alunos.route("/api/aluno", methods=['GET', 'POST', 'PUT', 'DELETE'])
def aluno():
    if request.method == 'GET':
        id = request.args.get('id')
        try:
            return jsonify(AlunoService.getbyid(id))
        except AssertionError as error:
            return str(error)
        
    if request.method == 'POST':    
        data = request.json
        
        ativo = data['ativo']
        nome = data['nome']
        curso = data['curso']
        ra = data['ra']
        turma = data['turma']

        try:
            return AlunoService.register(ativo, nome, ra, turma, curso)
        except AssertionError as error:
            return str(error)

    if request.method == 'PUT':
        id = request.args.get('id')
        data = request.json    

        ativo = data['ativo']
        nome = data['nome']
        ra = data['ra']
        turma_id = data['turma']
        curso = data['curso'] 

        try:
            return jsonify(AlunoService.update(id, ativo, nome, ra, turma_id, curso))
        except AssertionError as error:
                return str(error)
        
    if request.method == 'DELETE':
        id = request.args.get('id')
        try:
            return jsonify(AlunoService.delete(id))
        except AssertionError as error:
                return str(error)

@alunos.route("/api/aluno/listAll", methods=['GET'])
def listAll():
    return AlunoRepository.listAll()

@alunos.route("/api/aluno/findByRa", methods=['GET'])
def findByRa():
    ra = request.args.get('ra')
    try:
        return AlunoService.getByRa(ra)
    except AssertionError as error:
                return str(error)