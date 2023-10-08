from flask import jsonify
from models import db


from entity.Turma import Turma
from entity.Aluno import Aluno
from entity.Professor import Professor
from entity.TurmaAluno import turma_aluno
from entity.TurmaProfessor import turma_professor

class TurmaRepository():
    @staticmethod
    def get_turma_by_id(id):
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
    
    @staticmethod
    def list_all():
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
    
    @staticmethod
    def update(id, data):
        turma = Turma.query.get(id)

        turma.status = data.status
        turma.nome = data.nome
        turma.ano = data.ano
        turma.semestre = data.semestre
        turma.turno = data.turno
        turma.modalidade = data.modalidade
        turma.curso = data.curso

        db.session.merge(turma)
        db.session.commit()
        return f"Turma {id} atualizada com sucesso"

    @staticmethod
    def delete(id):
        turma = Turma.query.get(id)
        turma.status = False

        db.session.merge(turma)
        db.session.commit()

        return f"Turma {id} deletada com sucesso"

    @staticmethod  
    def register(turma):
        
        db.session.add(turma)
        db.session.commit()

        return f"Turma Cadastrada com o ID {turma.id_turma}!"
    
    @staticmethod
    def cadastrar_aluno(turma_id, aluno_id):

        aluno = db.session.query(Aluno).filter_by(id_aluno=aluno_id).first()

        turma = db.session.query(Turma).filter_by(id_turma=turma_id).first()

        if aluno is not None and turma is not None:

            db.session.execute(turma_aluno.insert().values(id_turma=turma_id, id_aluno=aluno_id))

            db.session.commit()
        else:
            print("Aluno ou Turma não encontrado")

        return "Aluno cadastrado na turma"
    
    @staticmethod
    def cadastrar_professor(turma_id, professor_id):

        professor = db.session.query(Professor).filter_by(id_professor=professor_id).first()

        turma = db.session.query(Turma).filter_by(id_turma=turma_id).first()

        if professor is not None and turma is not None:

            db.session.execute(turma_professor.insert().values(id_turma=turma_id, id_professor=professor_id))

            db.session.commit()
        else:
            print("Professor ou Turma não encontrado")

        return "Professor cadastrado na turma"