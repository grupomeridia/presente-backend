from flask import Blueprint, request, jsonify

from repository.MainRepository import MainRepository
from repository.AlunoRepository import AlunoRepository

from entity.Aluno import Aluno


alunos = Blueprint("alunos", __name__)

@alunos.route("/api/aluno", methods=['GET', 'POST', 'PUT', 'DELETE'])
def aluno():
    if request.method == 'GET':
        id = request.args.get('id')    
        return jsonify(AlunoRepository.getAlunoById(id))

    if request.method == 'POST':    
        data = request.json

        ativo = data['ativo']
        curso = data['curso']
        nome = data['nome']
        RA = data['ra']
        turma = data['turma']
        
        MainRepository.db.session.add(Aluno(ativo, nome, RA, turma, curso))
        MainRepository.db.session.commit()
        

        return "Aluno Cadastrado!"

    if request.method == 'PUT':
        id = request.args.get('id')
        data = request.json    
        return jsonify(AlunoRepository.update(id, data))
    
    if request.method == 'DELETE':
        id = request.args.get('id')
        return jsonify(AlunoRepository.delete(id))

@alunos.route("/api/aluno/listAll", methods=['GET'])
def listAll():
    return AlunoRepository.listAll()
