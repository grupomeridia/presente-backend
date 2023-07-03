from blueprints.AlunoBlueprint import alunos
from blueprints.ChamadaBlueprint import chamadas
from blueprints.PresencaBlueprint import presencas
from blueprints.ProfessorBlueprint import professores
from blueprints.ProjetoBlueprint import projetos
from blueprints.TurmaBlueprint import turmas
from blueprints.ConfiguracaoBlueprint import configuracoes

from repository.MainRepository import MainRepository

from flask import Flask, request, jsonify

with MainRepository.app.app_context():
    MainRepository.db.create_all()

MainRepository.app.register_blueprint(alunos)
MainRepository.app.register_blueprint(chamadas)
MainRepository.app.register_blueprint(presencas)
MainRepository.app.register_blueprint(professores)
MainRepository.app.register_blueprint(projetos)
MainRepository.app.register_blueprint(turmas)
MainRepository.app.register_blueprint(configuracoes)

MainRepository.app.run(debug=True, host="0.0.0.0")