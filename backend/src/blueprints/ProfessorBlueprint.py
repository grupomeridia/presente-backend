from flask import Blueprint, request, jsonify

from repository.ProfessorRepository import ProfessorRepository
from repository.MainRepository import MainRepository

from entity.Professor import Professor
from dtos.ProfessorDTO import ProfessorDTO

from service.ProfessorService import ProfessorService

professores = Blueprint("professores", __name__)

@professores.route("/api/professor", methods=['GET', 'POST', 'PUT', 'DELETE'])
def professor():
    if request.method == 'GET':
        id = request.args.get('id')
        try:
           return jsonify(ProfessorService.getProfessor(id))
        except AssertionError as error:
            return str(error)

    if request.method == 'POST':
        data = request.json

        id_usuario = data['idUsuario']
        status = True
        nome = data['nome']

        try:
            return ProfessorService.register(ProfessorDTO(id_usuario=id_usuario, status=status, nome=nome))
        except AssertionError as error:
            return str(error)        


    if request.method == 'PUT':
        id = request.args.get('id')
        data = request.json

        id_usuario = data['idUsuario']
        status = True
        nome = data['nome']

        try:
            return ProfessorService.update(id,ProfessorDTO(id_usuario=id_usuario, status=status, nome=nome))
        except AssertionError as error:
            return str(error)
        
    if request.method == 'DELETE':
        id = request.args.get("id")
        try:
            return jsonify(ProfessorRepository.delete(id))
        except AssertionError as error:
            return str(error)



@professores.route("/api/professor/listAll", methods=['GET'])
def listarAllProfessores():
   return ProfessorRepository.listAll()

@professores.route("/api/professor/cadastrado", methods=['GET'])
def listarTurmas():
    id = request.args.get("id")
    try:
        return ProfessorService.listarTurmas(id)
    except AssertionError as error:
        return str(error)
    
@professores.route("/api/professor/numAlunos", methods=['GET'])
def numAlunos():

    idProfessor = request.args.get("id_professor")
    idChamada = request.args.get("id_chamada")
    
    try:
        return ProfessorService.numAlunos(idProfessor, idChamada)
    except AssertionError as error:
        return str(error)
    
@professores.route("/api/professor/historico", methods=['GET'])
def historicoSemanal():
    idTurma = request.args.get("id")
    try:
        return ProfessorService.historicoSemanal(idTurma)
    except AssertionError as error:
        return str(error)
    
@professores.route("/api/professor/mediaSemanal", methods=['GET'])
def mediaSemanal():
    idTurma = request.args.get("id")
    try:
        return ProfessorService.mediaSemanal(idTurma)
    except AssertionError as error:
        return str(error)