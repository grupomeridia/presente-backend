from flask import Blueprint, request, jsonify

from repository.TurmaRepository import TurmaRepository

from entity.Turma import Turma
from dtos.TurmaDTO import TurmaDTO
from entity.TurnoEnum import Turno
from entity.ModalidadeEnum import Modalidade
from entity.CursoEnum import Curso

from service.TurmaService import TurmaService

turmas = Blueprint("turmas", __name__)

@turmas.route("/api/turma", methods=['GET', 'POST', 'PUT', 'DELETE'])
def turma():
    if request.method == 'GET':
        id_turma = request.args.get('id')
        try:
            return jsonify(TurmaService.get_turma(id_turma))
        except AssertionError as error:
            return str(error)

    if request.method == 'POST':
        data = request.json

        status = True
        nome = data.get('nome', 'NOT_FOUND')
        ano = data.get('ano', 'NOT_FOUND')
        semestre = data.get('semestre', 'NOT_FOUND')
        turno = data.get('turno', 'NOT_FOUND')
        modalidade = data.get('modalidade', 'NOT_FOUND')
        curso = data.get('curso', 'NOT_FOUND')

        if not turno or turno not in [turno.value for turno in Turno]:
            return jsonify({"error":"Campo 'turno' inválido."}), 400
        
        if not modalidade or modalidade not in [modalidade.value for modalidade in Modalidade]:
            return jsonify({"error":"Campo 'modalidade' inválido."}), 400
        
        if not curso or curso not in [curso.value for curso in Curso]:
            return jsonify({"error":"Campo 'curso' inválido."}), 400

        try:
            return TurmaService.post_turma(TurmaDTO(status=status, nome=nome, ano=ano, semestre=semestre, turno=turno, modalidade=modalidade, curso=curso))
        except AssertionError as error:
            return str(error)

    if request.method == 'PUT':
        id_turma = request.args.get('id')
        data = request.json

        status = True
        nome = data['nome']
        ano = data['ano']
        semestre = data['semestre']
        turno = data['turno']
        modalidade = data['modalidade']
        curso = data['curso']


        return TurmaService.update(id_turma, TurmaDTO(status=status, nome=nome, ano=ano, semestre=semestre, turno=turno, modalidade=modalidade, curso=curso))
    
    if request.method == 'DELETE':
        id_turma = request.args.get('id')

        try:
            return jsonify(TurmaService.delete(id_turma))
        except AssertionError as error:
            return str(error)

@turmas.route("/api/turma/listAll", methods=['GET'])
def listar_all_turmas():
    return TurmaRepository.list_all()

@turmas.route("/api/turma/cadastrarAluno", methods=['POST'])
def cadastrar_aluno():
    data = request.json

    id_turma = data['id_turma']
    id_aluno = data['id_aluno']

    return TurmaRepository.cadastrar_aluno(id_turma, id_aluno)

@turmas.route("/api/turma/cadastrarProfessor", methods=['POST'])
def cadastrar_professor():
    data = request.json

    id_turma = data['id_turma']
    id_professor = data['id_professor']

    return TurmaRepository.cadastrar_professor(id_turma, id_professor)