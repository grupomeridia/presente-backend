from flask import Blueprint, request, jsonify

from repository.AlunoRepository import AlunoRepository
from flask_jwt_extended import jwt_required

from service.AlunoService import AlunoService

alunos = Blueprint("alunos", __name__)

@alunos.route("/api/aluno", methods=['GET', 'POST', 'PUT', 'DELETE'])
def aluno():
    if request.method == 'GET':
        id_aluno = request.args.get('id')
        try:
            return jsonify(AlunoService.get_by_id(id_aluno))
        except AssertionError as error:
            return str(error), 400
        
    if request.method == 'POST':    
        data = request.json
        
        id_usuario = data.get('id_usuario', 'NOT_FOUND')
        nome = data.get('nome', 'NOT_FOUND')
        ra = data.get('ra', 'NOT_FOUND')

        status = True
        ausente = False
        
        try:
            return AlunoService.register(id_usuario=id_usuario, status=status, nome=nome, ra=ra, ausente=ausente)
        except AssertionError as error:
            return str(error), 400

    if request.method == 'PUT':
        id_aluno = request.args.get('id')
        data = request.json    

        nome = data.get('nome', 'NOT_FOUND')
        ra = data.get('ra', 'NOT_FOUND')

        status = True
        ausente = False

        try:
            return AlunoService.update(id_aluno=id_aluno, status=status, nome=nome, ra=ra, ausente=ausente)
        except AssertionError as error:
            return str(error), 400
        
    if request.method == 'DELETE':
        id_aluno = request.args.get('id')
        try:
            return jsonify(AlunoService.delete(id_aluno))
        except AssertionError as error:
            return str(error), 400

@alunos.route("/api/aluno/listAll", methods=['GET'])
def list_all():
    return AlunoRepository.list_all()

@alunos.route("/api/aluno/findByRa", methods=['GET'])
def find_by_ra():
    ra = request.args.get('ra')
    try:
        return AlunoService.get_by_ra(ra)
    except AssertionError as error:
        return str(error), 400
    
@alunos.route("/api/aluno/AusentesPresentes", methods=['GET'])
def ausentes_presentes():
    turma_id = request.args.get('id_turma')
    try:
        return AlunoService.ausentes_presentes(turma_id)
    except AssertionError as error:
        return str(error), 400
    
@alunos.route("/api/aluno/AtivoInativo", methods=['GET'])
def ativo_inativo():
    turma_id = request.args.get('id_turma')
    try:
        return AlunoService.ativo_inativo(turma_id)
    except AssertionError as error:
        return str(error), 400
    
@alunos.route("/api/aluno/mediaAtivo", methods=['GET'])
def media_ativo():
    turma_id = request.args.get('id_turma')
    try:
        return AlunoService.media_ativo(turma_id)
    except AssertionError as error:
        return str(error), 400
    
@alunos.route("/api/aluno/mediaAusente", methods=['GET'])
def media_ausente():
    turma_id = request.args.get('id_turma')
    
    try:
        return AlunoService.media_ausente(turma_id)
    except AssertionError as error:
        return str(error), 400

@alunos.route("/api/aluno/HistoricoPresenca", methods=['GET'])
@jwt_required()
def historico_presenca():
    id_aluno = request.args.get('id_aluno')
    try:
        return AlunoService.historico_presenca(id_aluno)
    except AssertionError as error:
        return str(error), 400

@alunos.route("/api/aluno/PresencaFalta", methods=['GET'])
def presenca_falta():
    id_aluno = request.args.get('id_aluno')
    try:
        return AlunoService.presenca_falta(id_aluno)
    except AssertionError as error:
        return str(error), 400
    
@alunos.route("/api/aluno/ausentes", methods=['GET'])
def alunos_ausentes():
    try:
        return AlunoRepository.alunos_ausentes()
    except AssertionError as error:
        return str(error), 400
    
@alunos.route("/api/aluno/presentes", methods=['GET'])
def alunos_presentes():
    try:
        return AlunoRepository.alunos_presentes()
    except AssertionError as error:
        return str(error), 400
    
@alunos.route("/api/aluno/chegar", methods=['GET'])
def alunos_a_chegar():
    try:
        return AlunoRepository.alunos_a_chegar()
    except AssertionError as error:
        return str(error), 400
    
@alunos.route("/api/aluno/alunoStatus", methods=['GET'])
def aluno_status():
    id_aluno = request.args.get('id_aluno')
    try:
        return AlunoService.aluno_status(id_aluno)
    except AssertionError as error:
        return str(error), 400
    
@alunos.route("/api/aluno/turmaPresenca", methods=['GET'])
def alunos_presenca_turma():
    turma_id = request.args.get('turma_id')
    try:
        return AlunoRepository.alunos_presenca_turma(turma_id)
    except AssertionError as error:
        return str(error), 400