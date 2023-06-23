from flask import Blueprint, request, jsonify

from repository.MainRepository import MainRepository
from repository.TurmaRepository import TurmaRepository

from entity.Turma import Turma

turmas = Blueprint("turmas", __name__)

@turmas.route("/api/turma/cadastrar", methods=['POST'])
def cadastrarTurma():
    data = request.json

    ativo = data['ativo']
    nome = data['nome']
    ano = data['ano']
    semestre = data['semestre']

    MainRepository.db.session.add(Turma(ativo, nome, ano, semestre))
    MainRepository.db.session.commit()

    return "Turma Cadastrada!"

@turmas.route("/api/turma/findById", methods=['GET'])
def listarTurmas():
    id = request.args.get('id')
    print(TurmaRepository.getTurmaById(id))
    return jsonify(TurmaRepository.getTurmaById(id))