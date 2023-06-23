from flask import Blueprint, request, jsonify

from repository.MainRepository import MainRepository
from repository.PresencaRepository import PresencaRepository

from entity.Presenca import Presenca

presencas = Blueprint("presencas", __name__)

@presencas.route("/api/presenca/cadastrar", methods=['POST'])
def cadastrarPresente():
    data = request.json

    ativo = data['ativo']
    aluno_ra = data['aluno_ra']
    turma = data['turma']
    projeto = data['projeto']
    chamada = data['chamada']
    professor = data['professor']
    tipo_presenca = data['tipo_presenca']
    horario = data['horario']

    MainRepository.db.session.add(Presenca(ativo, aluno_ra, turma, projeto, chamada, professor, tipo_presenca, horario))
    MainRepository.db.session.commit()

    return "Presenca Cadastrada!"

@presencas.route("/api/presenca/findById", methods=['GET'])
def listarPresenca():
    id = request.args.get('id')

    return jsonify(PresencaRepository.getAlunoById(id))

@presencas.route("/api/presenca/listAll", methods=['GET'])
def listAllPresencas():
    return PresencaRepository.listAll()

@presencas.route("/api/presenca/findByPresentes", methods=['GET'])
def findByPresentes():
    return PresencaRepository.findByPresentes()