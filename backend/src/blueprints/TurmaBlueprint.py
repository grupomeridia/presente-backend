from flask import Blueprint, request, jsonify

from repository.TurmaRepository import TurmaRepository

from service.TurmaService import TurmaService

turmas = Blueprint("turmas", __name__)

@turmas.route("/api/turma", methods=['GET', 'POST', 'PUT', 'DELETE'])
def turma():
    if request.method == 'GET':
        id_turma = request.args.get('id')
        try:
            return jsonify(TurmaService.get_turma(id_turma))
        except AssertionError as error:
            return str(error), 400 

    if request.method == 'POST':
        data = request.json
        
        status = True
        id_materia = data.get('id_materia', 'NOT_FOUND')
        nome = data.get('nome', 'NOT_FOUND')
        ano = data.get('ano', 'NOT_FOUND')
        semestre = data.get('semestre', 'NOT_FOUND')
        turno = data.get('turno', 'NOT_FOUND')
        modalidade = data.get('modalidade', 'NOT_FOUND')
        curso = data.get('curso', 'NOT_FOUND')

        try:
            return TurmaService.post_turma(status, id_materia, nome, ano, semestre, turno, modalidade, curso)
        except AssertionError as error:
            return str(error), 400

    if request.method == 'PUT':
        id_turma = request.args.get('id')
        data = request.json

        status = True
        id_materia = data.get('id_materia', 'NOT_FOUND')
        nome = data.get('nome', 'NOT_FOUND')
        ano = data.get('ano', 'NOT_FOUND')
        semestre = data.get('semestre', 'NOT_FOUND')
        turno = data.get('turno', 'NOT_FOUND')
        modalidade = data.get('modalidade', 'NOT_FOUND')
        curso = data.get('curso', 'NOT_FOUND')

        return TurmaService.update(id_turma=id_turma, id_materia=id_materia, status=status, nome=nome, ano=ano, semestre=semestre, turno=turno, modalidade=modalidade, curso=curso)
    
    if request.method == 'DELETE':
        id_turma = request.args.get('id')

        try:
            return jsonify(TurmaService.delete(id_turma))
        except AssertionError as error:
            return str(error), 400

@turmas.route("/api/turma/listAll", methods=['GET'])
def listar_all_turmas():
    return TurmaRepository.list_all()

@turmas.route("/api/turma/cadastrarAluno", methods=['POST'])
def cadastrar_aluno():
    data = request.json

    id_turma = data['id_turma']
    id_aluno = data['id_aluno']

    try:
        return TurmaService.cadastrar_aluno(id_turma, id_aluno)
    except AssertionError as error:
        return str(error), 400

@turmas.route("/api/turma/cadastrarProfessor", methods=['POST'])
def cadastrar_professor():
    data = request.json

    id_turma = data['id_turma']
    id_professor = data['id_professor']

    try:
        return TurmaService.cadastrar_professor(id_turma, id_professor)
    except AssertionError as error:
        return str(error), 400