from blueprints.AlunoBlueprint import alunos
from blueprints.ChamadaBlueprint import chamadas
from blueprints.LembreteBlueprint import lembretes
from blueprints.PainelBlueprint import paineis
from blueprints.PresencaBlueprint import presencas
from blueprints.ProfessorBlueprint import professores
from blueprints.SecretariaBlueprint import secretaria
from blueprints.MateriaBlueprint import materias
from blueprints.TurmaBlueprint import turmas
from blueprints.UsuarioBlueprint import usuarios
from blueprints.ConfiguracaoBlueprint import configuracoes

from repository.MainRepository import MainRepository

from flask import Flask, request, jsonify


MainRepository.app.register_blueprint(alunos)
MainRepository.app.register_blueprint(chamadas)
MainRepository.app.register_blueprint(lembretes)
MainRepository.app.register_blueprint(paineis)
MainRepository.app.register_blueprint(presencas)
MainRepository.app.register_blueprint(professores)
MainRepository.app.register_blueprint(secretaria)
MainRepository.app.register_blueprint(materias)
MainRepository.app.register_blueprint(turmas)
MainRepository.app.register_blueprint(usuarios)
MainRepository.app.register_blueprint(configuracoes)

MainRepository.app.run(debug=True, host="0.0.0.0")