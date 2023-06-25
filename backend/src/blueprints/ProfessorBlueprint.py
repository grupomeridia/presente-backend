from flask import Blueprint, request, jsonify

from repository.ProfessorRepository import ProfessorRepository
from repository.MainRepository import MainRepository

from entity.Professor import Professor

professores = Blueprint("professores", __name__)

@professores.route("/api/professor", methods=['GET', 'POST', 'PUT', 'DELETE'])
def professor():
   if request.method == 'GET':
       id = request.args.get('id')


       return jsonify(ProfessorRepository.getProfessorById(id))


   if request.method == 'POST':
       data = request.json


       ativo = data['ativo']
       nome = data['nome']


       MainRepository.db.session.add(Professor(ativo, nome))
       MainRepository.db.session.commit()


       return "Professor Cadastrado!"


   if request.method == 'PUT':
       id = request.args.get('id')
       data = request.json
       return jsonify(ProfessorRepository.update(id, data))
  
   if request.method == 'DELETE':
       id = request.args.get("id")
       return jsonify(ProfessorRepository.delete(id))




@professores.route("/api/professor/listAll", methods=['GET'])
def listarAllProfessores():
   return ProfessorRepository.listAll()