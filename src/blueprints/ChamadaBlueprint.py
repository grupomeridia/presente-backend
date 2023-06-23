from flask import Blueprint, request, jsonify

from repository.MainRepository import MainRepository
from repository.ChamadaRepository import ChamadaRepository

from entity.Chamada import Chamada

chamadas = Blueprint("chamadas", __name__)

@chamadas.route("/api/chamada/cadastrar", methods=['POST'])
def cadastrarChamada():
    data = request.json

    ativo = data['ativo']
    projeto = data['projeto']
    professor = data['professor']
    turma = data['turma']

    MainRepository.db.session.add(Chamada(ativo, projeto, professor, turma))
    MainRepository.db.session.commit()

    return "Chamada Cadastrada!"

@chamadas.route("/api/chamada/findById", methods=['GET'])
def listarChamada():
    id = request.args.get('id')

    return jsonify(ChamadaRepository.getChamadaById(id))

@chamadas.route("/api/chamada/listAll", methods=['GET'])
def listarAllChamadas():
    return ChamadaRepository.listAll()
