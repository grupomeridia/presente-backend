from flask import Blueprint, request, jsonify

from repository.MateriaRepository import MateriaRepository
from dtos.MateriaDTO import MateriaDTO

from service.MateriaService import MateriaService

materias = Blueprint("Materia", __name__)   

@materias.route("/api/materia", methods=['GET', 'POST','PUT','DELETE'])
def materia():
    if request.method == 'GET':
        id = request.args.get('id')
        try:    
            return jsonify(MateriaService.getMateria(id))
        except AssertionError as error:
            return str(error)
    
    if request.method == 'POST':
        data = request.json
    
        status = True
        nome = data['nome']

        try:
            return MateriaService.register(MateriaDTO(status=status, nome=nome))
        except AssertionError as error:
            return str(error)
    
    if request.method == 'PUT':
        id = request.args.get('id')
        data = request.json

        status = True
        nome = data['nome']

        try: 
            return jsonify(MateriaRepository.update(MateriaDTO(status=status, nome=nome)))
        except AssertionError as error:
            return str(error)
    
    if request.method == 'DELETE':
        id = request.args.get('id')
        try:
            return jsonify(MateriaRepository.delete(id))
        except AssertionError as error:
            return str(error)
    
@materias.route("/api/materia/listAll", methods=['GET'])
def listarAllMaterias():
    return MateriaRepository.listAll()