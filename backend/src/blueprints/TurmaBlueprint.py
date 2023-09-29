from flask import Blueprint, request, jsonify

from repository.MainRepository import MainRepository
from repository.TurmaRepository import TurmaRepository

from entity.Turma import Turma
from dtos.TurmaDTO import TurmaDTO

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

        status = True
        nome = data['nome']
        ano = data['ano']
        semestre = data['semestre']
        turno = data['turno']
        modalidade = data['modalidade']
        curso = data['curso']

        try:
            return TurmaService.postTurma(TurmaDTO(status=status, nome=nome, ano=ano, semestre=semestre, turno=turno, modalidade=modalidade, curso=curso))
        except AssertionError as error:
            return str(error)

    if request.method == 'PUT':
        id = request.args.get('id')
        data = request.json

        status = True
        nome = data['nome']
        ano = data['ano']
        semestre = data['semestre']
        turno = data['turno']
        modalidade = data['modalidade']
        curso = data['curso']


        return TurmaService.update(id, TurmaDTO(status=status, nome=nome, ano=ano, semestre=semestre, turno=turno, modalidade=modalidade, curso=curso))
    
    if request.method == 'DELETE':
        id = request.args.get('id')
        return jsonify(TurmaService.delete(id))

@turmas.route("/api/turma/listAll", methods=['GET'])
def listarAllTurmas():
    return TurmaRepository.listAll()

@turmas.route("/api/turma/cadastrarAluno", methods=['POST'])
def cadastrarAluno():
    data = request.json

    id_turma = data['idTurma']
    id_aluno = data['idAluno']

    return TurmaRepository.cadastrarAluno(id_turma, id_aluno)

@turmas.route("/api/turma/cadastrarProfessor", methods=['POST'])
def cadastrarProfessor():
    data = request.json

    id_turma = data['idTurma']
    id_professor = data['idProfessor']

    return TurmaRepository.cadastrarProfessor(id_turma, id_professor)