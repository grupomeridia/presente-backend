from entity.Aluno import Aluno
from entity.Chamada import Chamada
from entity.Configuracao import Configuracao
from entity.CursoEnum import Curso
from entity.Presenca import Presenca
from entity.PresencaEnum import TipoPresenca
from entity.Professor import Professor
from entity.Turma import Turma
from entity.Projeto import Projeto

from repository.MainRepository import MainRepository
from repository.TurmaRepository import TurmaRepository
from repository.AlunoRepository import AlunoRepository
from repository.ProfessorRepository import ProfessorRepository
from repository.ProjetoRepository import ProjetoRepository
from repository.ChamadaRepository import ChamadaRepository
from repository.PresencaRepository import PresencaRepository
from flask import Flask, request, jsonify

with MainRepository.app.app_context():
    MainRepository.db.create_all()


@MainRepository.app.route("/api/aluno/cadastrar", methods=["POST"])
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

@MainRepository.app.route("/api/aluno/findById", methods=['GET'])
def listarAlunos():
    id = request.args.get('id')
    
    return jsonify(AlunoRepository.getAlunoById(id))

@MainRepository.app.route("/api/aluno/listAll", methods=['GET'])
def listAllAlunos():
    return AlunoRepository.listAll()

@MainRepository.app.route("/api/turma/cadastrar", methods=['POST'])
def cadastrarTurma():
    data = request.json

    ativo = data['ativo']
    nome = data['nome']
    ano = data['ano']
    semestre = data['semestre']

    MainRepository.db.session.add(Turma(ativo, nome, ano, semestre))
    MainRepository.db.session.commit()

    return "Turma Cadastrada!"

@MainRepository.app.route("/api/turma/findById", methods=['GET'])
def listarTurmas():
    id = request.args.get('id')
    print(TurmaRepository.getTurmaById(id))
    return jsonify(TurmaRepository.getTurmaById(id))
    
#Rotas do Professor
@MainRepository.app.route("/api/professor/cadastrar", methods=['POST'])
def cadastrarProfessor():
    data = request.json

    ativo = data['ativo']
    nome = data['nome']

    MainRepository.db.session.add(Professor(ativo, nome))
    MainRepository.db.session.commit()

    return "Professor Cadastrado!"

@MainRepository.app.route("/api/professor/findById", methods=['GET'])
def listarProfessor():
    id = request.args.get('id')

    return jsonify(ProfessorRepository.getProfessorById(id)) 


@MainRepository.app.route("/api/professor/listAll", methods=['GET'])
def listarAllProfessores():
    return ProfessorRepository.listAll()

#Rotas de Projeto
@MainRepository.app.route("/api/projeto/cadastrar", methods=['POST'])
def cadastrarProjeto():
    data = request.json

    ativo = data['ativo']
    nome = data['nome']

    MainRepository.db.session.add(Projeto(ativo, nome))
    MainRepository.db.session.commit()

    return "Projeto Cadastrado!"

@MainRepository.app.route("/api/projeto/findById", methods=['GET'])
def listarProjeto():
    id = request.args.get('id')

    return jsonify(ProjetoRepository.getProjetoById(id))

@MainRepository.app.route("/api/projeto/listAll", methods=['GET'])
def listarAllProjetos():
    return ProjetoRepository.listAll()

#Rotas de Chamada
@MainRepository.app.route("/api/chamada/cadastrar", methods=['POST'])
def cadastrarChamada():
    data = request.json

    ativo = data['ativo']
    projeto = data['projeto']
    professor = data['professor']
    turma = data['turma']

    MainRepository.db.session.add(Chamada(ativo, projeto, professor, turma))
    MainRepository.db.session.commit()

    return "Chamada Cadastrada!"

@MainRepository.app.route("/api/chamada/findById", methods=['GET'])
def listarChamada():
    id = request.args.get('id')

    return jsonify(ChamadaRepository.getChamadaById(id))

@MainRepository.app.route("/api/chamada/listAll", methods=['GET'])
def listarAllChamadas():
    return ChamadaRepository.listAll()


@MainRepository.app.route("/api/presenca/cadastrar", methods=['POST'])
def cadastrarPresente():
    data = request.json

    ativo = data['ativo']
    aluno_ra = data['aluno_ra']
    turma = data['turma']
    projeto = data['projeto']
    chamada = data['chamada']
    professor = data['professor']
    tipo_presenca = data['tipo_presenca']
    horario = data['horario']

    MainRepository.db.session.add(Presenca(ativo, aluno_ra, turma, projeto, chamada, professor, tipo_presenca, horario))
    MainRepository.db.session.commit()

    return "Presenca Cadastrada!"

@MainRepository.app.route("/api/presenca/findById", methods=['GET'])
def listarPresenca():
    id = request.args.get('id')

    return jsonify(PresencaRepository.getAlunoById(id))

@MainRepository.app.route("/api/presenca/listAll", methods=['GET'])
def listAllPresencas():
    return PresencaRepository.listAll()

@MainRepository.app.route("/api/presenca/findByPresentes", methods=['GET'])
def findByPresentes():
    return PresencaRepository.findByPresentes()

MainRepository.app.run(debug=True)