from entity.Aluno import Aluno
from entity.Chamada import Chamada
from entity.Configuracao import Configuracao
from entity.CursoEnum import Curso
from entity.Presenca import Presenca
from entity.PresencaEnum import TipoPresenca
from entity.Professor import Professor
from entity.Turma import Turma

from repository.MainRepository import MainRepository
from repository.TurmaRepository import TurmaRepository

from flask import Flask, request, jsonify

with MainRepository.app.app_context():
    MainRepository.db.create_all()


@MainRepository.app.route("/api/cadastrarAluno", methods=["POST"])
def cadastrarAluno():
    data = request.json

    ativo = data['ativo']
    curso = data['curso']
    nome = data['nome']
    RA = data['ra']
    turma = data['turma']
    
    return data


@MainRepository.app.route("/api/cadastrarTurma", methods=['POST'])
def cadastrarTurma():
    data = request.json

    ativo = data['ativo']
    nome = data['nome']
    ano = data['ano']
    semestre = data['semestre']

    MainRepository.db.session.add(Turma(ativo, nome, ano, semestre))
    MainRepository.db.session.commit()

    return "Turma Cadastrada!"

MainRepository.app.run(debug=True)