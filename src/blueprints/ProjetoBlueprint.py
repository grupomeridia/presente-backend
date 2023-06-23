from flask import Blueprint, request, jsonify

from repository.MainRepository import MainRepository
from repository.ProjetoRepository import ProjetoRepository

from entity.Projeto import Projeto

projetos = Blueprint("projetos", __name__)

@projetos.route("/api/projeto/cadastrar", methods=['POST'])
def cadastrarProjeto():
    data = request.json

    ativo = data['ativo']
    nome = data['nome']

    MainRepository.db.session.add(Projeto(ativo, nome))
    MainRepository.db.session.commit()

    return "Projeto Cadastrado!"

@projetos.route("/api/projeto/findById", methods=['GET'])
def listarProjeto():
    id = request.args.get('id')

    return jsonify(ProjetoRepository.getProjetoById(id))

@projetos.route("/api/projeto/listAll", methods=['GET'])
def listarAllProjetos():
    return ProjetoRepository.listAll()