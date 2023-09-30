from flask import Blueprint, request, jsonify

from repository.AlunoRepository import AlunoRepository
from dtos.AlunoDTO import AlunoDTO
from entity.Aluno import Aluno

from service.AlunoService import AlunoService

alunos = Blueprint("alunos", __name__)

@alunos.route("/api/aluno", methods=['GET', 'POST', 'PUT', 'DELETE'])
def aluno():
    if request.method == 'GET':
        id_aluno = request.args.get('id')
        try:
            return jsonify(AlunoService.get_by_id(id_aluno))
        except AssertionError as error:
            return str(error)
        
    if request.method == 'POST':    
        data = request.json
        
        id_usuario = data['id_usuario']
        status = True
        ausente = True
        nome = data['nome']
        ra = data['ra']
        

        try:
            return AlunoService.register(AlunoDTO(id_usuario=id_usuario, status=status, nome=nome, ra=ra, ausente=ausente))
        except AssertionError as error:
            return str(error)

    if request.method == 'PUT':
        id_aluno = request.args.get('id')
        data = request.json    

        id_usuario = data['id_usuario']
        status = True
        ausente = True
        nome = data['nome']
        ra = data['ra']

        try:
            return AlunoService.update(id_aluno, AlunoDTO(id_usuario=id_usuario, status=status, nome=nome, ra=ra, ausente=ausente))
        except AssertionError as error:
            return str(error)
        
    if request.method == 'DELETE':
        id_aluno = request.args.get('id')
        try:
            return jsonify(AlunoService.delete(id_aluno))
        except AssertionError as error:
            return str(error)

@alunos.route("/api/aluno/listAll", methods=['GET'])
def list_all():
    return AlunoRepository.list_all()

@alunos.route("/api/aluno/findByRa", methods=['GET'])
def find_by_ra():
    ra = request.args.get('ra')
    try:
        return AlunoService.get_by_ra(ra)
    except AssertionError as error:
                return str(error)