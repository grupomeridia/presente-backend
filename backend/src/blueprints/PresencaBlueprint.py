from flask import Blueprint, request, jsonify

from repository.MainRepository import MainRepository
from repository.PresencaRepository import PresencaRepository

from entity.Presenca import Presenca

presencas = Blueprint("presencas", __name__)

@presencas.route("/api/presenca", methods=['GET', 'POST', 'PUT', 'DELETE'])
def presencasMain():
    if request.method == 'GET':
        id = request.args.get('id')
        return jsonify(PresencaRepository.getPresencaById(id))
    
    if request.method == 'POST':
        data = request.json

        ativo = data['ativo']
        aluno_ra = data['AlunoRa']
        turma = data['turma']
        projeto = data['projeto']
        chamada = data['chamada']
        professor = data['professor']
        tipo_presenca = data['tipoPresenca']
        horario = data['horario']

        MainRepository.db.session.add(Presenca(ativo, aluno_ra, turma, projeto, chamada, professor, tipo_presenca, horario))
        MainRepository.db.session.commit()

        return "Presenca Cadastrada!"    
    
    if request.method == 'PUT':
        id = request.args.get('id')
        data = request.json

        return PresencaRepository.update(id,data)
    
    if request.method == 'DELETE':
        id = request.args.get('id')
        return PresencaRepository.delete(id)

@presencas.route("/api/presenca/listAll", methods=['GET'])
def listAll():
    return PresencaRepository.listAll()

@presencas.route("/api/presenca/findByPresentes", methods=['GET'])
def findByPresentes():
    return PresencaRepository.findByPresentes()