from flask import Blueprint, request, jsonify

from repository.ProfessorRepository import ProfessorRepository
from repository.MainRepository import MainRepository

from entity.Professor import Professor

professores = Blueprint("professores", __name__)

@professores.route("/api/professor/cadastrar", methods=['POST'])
def cadastrarProfessor():
    data = request.json

    ativo = data['ativo']
    nome = data['nome']

    MainRepository.db.session.add(Professor(ativo, nome))
    MainRepository.db.session.commit()

    return "Professor Cadastrado!"

@professores.route("/api/professor/findById", methods=['GET'])
def listarProfessor():
    id = request.args.get('id')

    return jsonify(ProfessorRepository.getProfessorById(id)) 


@professores.route("/api/professor/listAll", methods=['GET'])
def listarAllProfessores():
    return ProfessorRepository.listAll()