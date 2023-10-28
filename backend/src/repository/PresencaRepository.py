from flask import jsonify
from models import db

from entity.Presenca import Presenca
from entity.Aluno import Aluno
from repository.ChamadaRepository import ChamadaRepository
from datetime import datetime

class PresencaRepository():
    @staticmethod
    def get_presenca_by_id(id):

        try:
            return {
                "id_presenca" : Presenca.query.get(id).id_presenca,
                "aluno": Presenca.query.get(id).id_aluno,
                "chamada": Presenca.query.get(id).id_chamada,
                "status": Presenca.query.get(id).status,
                "tipo_presenca": Presenca.query.get(id).tipo_presenca.value,
                "horario": Presenca.query.get(id).horario
            }
        except AttributeError as error:
            print(f"{str(error)}")
            raise AssertionError ("Prensença não existe.")
    
    @staticmethod
    def list_all():
        presencas = Presenca.query.all()
        resultado = [{
            "Id": p.id,
            "Aluno": p.idAluno.nome,
            "Chamada": p.idChamada,
            "status": p.status,
            "Tipo_presenca": p.tipoPresenca.value,
            "Horario": p.horario
        } for p in presencas]

        return jsonify(resultado)
    
    @staticmethod
    def find_by_presentes():
        presencas = Presenca.query.filter(Presenca.horario.isnot(None)).all()

        resultado = [{
            "Id": p.id,
            "Aluno": p.idAluno.nome,
            "Chamada": p.idChamada,
            "status": p.status,
            "Tipo_presenca": p.tipoPresecna.value,
            "Horario": p.horario
        } for p in presencas]

        return jsonify(resultado)
    
    @staticmethod
    def update(id, data):
        presenca = Presenca.query.get(id)

        presenca.id_aluno = data.id_aluno
        presenca.id_hamada = data.id_chamada
        presenca.status = data.status
        presenca.tipo_presenca = data.tipo_presenca
        presenca.horario = data.horario

        db.session.merge(presenca)
        db.session.commit()
        
        return f"Presenca {id} atualizada!"

    @staticmethod
    def delete(id):
        presenca = Presenca.query.get(id)
        presenca.status = False
        db.session.merge(presenca)
        db.session.commit()

        return {"mensagem":"sucesso"}
    
    @staticmethod
    def marcar_presenca_pelo_ra(ra):
        aluno = db.text(""" Select * from alunos where ra = :ra """)
        
        with db.engine.connect() as connection:
            valor = connection.execute(aluno, {'ra': ra}).fetchone()
      
        valor2 = ChamadaRepository.get_chamadas_abertas_aluno(valor.id_aluno)
        print(valor2)
    
        if not valor2:
            return "Não existe chamada aberta para esse aluno"

        id_aluno = valor.id_aluno

        id_chamada = valor2[0]['id_chamada']

        presenca = db.text(""" SELECT * FROM presencas where id_aluno = :id_aluno and id_chamada = :id_chamada""")
        
        with db.engine.connect() as connection:
            resultado = connection.execute(presenca, {'id_aluno':id_aluno, 'id_chamada':id_chamada}).fetchone()
        
            if resultado is not None:
                return "Presenca já registrada"

        presenca = Presenca(id_aluno=id_aluno, id_chamada=id_chamada, status=True, horario=datetime.now(), tipo_presenca='Manual')
        db.session.add(presenca)
        db.session.commit()

        return {"mensagem": "presenca registrada"}

    @staticmethod
    def register_presenca(presenca):

        db.session.add(presenca)
        db.session.commit()

        return "Presença realizada!"