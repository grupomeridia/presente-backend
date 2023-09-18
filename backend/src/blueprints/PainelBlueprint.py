from flask import Blueprint, request, jsonify

from service.PainelService import PainelService

painel = Blueprint("painel", __name__)

@painel.route("/api/painel", methods=['GET'])
def painel():
    if request.method == 'GET':
        pass