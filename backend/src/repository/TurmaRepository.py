from flask import jsonify
from repository.MainRepository import MainRepository


from entity.Turma import Turma
from entity.Aluno import Aluno
from entity.Professor import Professor
from entity.TurmaAluno import turma_aluno
from entity.TurmaProfessor import turma_professor

class TurmaRepository():
    def getTurmaById(id):
        return {
               "Id":Turma.query.get(id).id_turma,
               "status":Turma.query.get(id).status,
               "nome": Turma.query.get(id).nome,
               "Ano": Turma.query.get(id).ano,
               "Semestre": Turma.query.get(id).semestre,
               "turno": Turma.query.get(id).turno.value,
               "modalidade": Turma.query.get(id).modalidade.value,
               "curso": Turma.query.get(id).curso.value
               } 
    
    def listAll():
        turmas = Turma.query.all()
        resultado = [{
            "Id": t.id_turma,
            "status": t.status,
            "Nome": t.nome,
            "Ano": t.ano,
            "Semestre": t.semestre,
            "turno": t.turno.value,
            "modalidade": t.modalidade.value,
            "curso": t.curso.value
        } for t in turmas]

        return jsonify(resultado)
    
    def update(id, data):
        turma = Turma.query.get(id)

        turma.status = data.status
        turma.nome = data.nome
        turma.ano = data.ano
        turma.semestre = data.semestre
        turma.turno = data.turno
        turma.modalidade = data.modalidade
        turma.curso = data.curso

        MainRepository.db.session.merge(turma)
        MainRepository.db.session.commit()
        return {"mensagem":"sucesso"}

    def delete(id):
        turma = Turma.query.get(id)
        turma.ativo = False

        MainRepository.db.session.merge(turma)
        MainRepository.db.session.commit()

        return {"mensagem":"sucesso"}
           
    def register(turma):
        
        MainRepository.db.session.add(turma)
        MainRepository.db.session.commit()

        return f"Turma Cadastrada com o ID {turma.id_turma}!"
    
    def cadastrarAluno(idTurma, idAluno):

        aluno = MainRepository.db.session.query(Aluno).filter_by(id_aluno=idAluno).first()

        turma = MainRepository.db.session.query(Turma).filter_by(id_turma=idTurma).first()

        if aluno is not None and turma is not None:

            MainRepository.db.session.execute(turma_aluno.insert().values(id_turma=idTurma, id_aluno=idAluno))

            MainRepository.db.session.commit()
        else:
            print("Aluno ou Turma não encontrado")

        return "Aluno cadastrado na turma"
    
    def cadastrarProfessor(idTurma, idProfessor):

        professor = MainRepository.db.session.query(Professor).filter_by(id_professor=idProfessor).first()

        turma = MainRepository.db.session.query(Turma).filter_by(id_turma=idTurma).first()

        if professor is not None and turma is not None:

            MainRepository.db.session.execute(turma_professor.insert().values(id_turma=idTurma, id_professor=idProfessor))

            MainRepository.db.session.commit()
        else:
            print("Professor ou Turma não encontrado")

        return "Professor cadastrado na turma"