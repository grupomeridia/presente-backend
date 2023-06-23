from flask import Blueprint, request, jsonify

from repository.MainRepository import MainRepository
from repository.AlunoRepository import AlunoRepository

from entity.Aluno import Aluno


alunos = Blueprint("alunos", __name__)

@alunos.route("/api/aluno/cadastrar", methods=["POST"])
def cadastrarAluno():
    data = request.json

    ativo = data['ativo']
    curso = data['curso']
    nome = data['nome']
    RA = data['ra']
    turma = data['turma']
    
    MainRepository.db.session.add(Aluno(ativo, nome, RA, turma, curso))
    MainRepository.db.session.commit()
    

    return "Aluno Cadastrado!"

@alunos.route("/api/aluno/findById", methods=['GET'])
def findById():
    id = request.args.get('id')
    
    return jsonify(AlunoRepository.getAlunoById(id))

@alunos.route("/api/aluno/listAll", methods=['GET'])
def listAll():
    return AlunoRepository.listAll()

@alunos.route("/api/aluno", methods=['PUT'])
def update():
    id = request.args.get('id')
    data = request.json    
    return jsonify(AlunoRepository.update(id, data))