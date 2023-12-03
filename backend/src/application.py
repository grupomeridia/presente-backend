from flask import Flask
from flask_cors import CORS
from models import login_manager

def create_app(config_file):
    

    from models import db
    from flask_login import LoginManager
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
    from flask_wtf.csrf import CSRFProtect
    from flask_jwt_extended import JWTManager


    app = Flask(__name__)
    CORS(app)
    # CSRFProtect(app)
    
    app.config.from_pyfile(config_file)   

    jwt = JWTManager(app)

    app.register_blueprint(alunos)
    app.register_blueprint(chamadas)
    app.register_blueprint(lembretes)
    app.register_blueprint(paineis)
    app.register_blueprint(presencas)
    app.register_blueprint(professores)
    app.register_blueprint(secretaria)
    app.register_blueprint(materias)
    app.register_blueprint(turmas)
    app.register_blueprint(usuarios)
    app.register_blueprint(configuracoes)

    
    db.init_app(app)
    
    
    login_manager.init_app(app)

    return app





