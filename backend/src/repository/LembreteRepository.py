from flask import jsonify
from repository.MainRepository import MainRepository
from entity.CargoEnum import Cargo
from entity.Lembrete import Lembrete

class LembreteRepository():
    
    def getLembreteById(id):
        return {
            "IdLembrete": Lembrete.query.get(id).id,
            "DestinatarioId": Lembrete.query.get(id).destinatarioId,
            "DestinatarioCargo": Lembrete.query.get(id).destinatarioCargo,
            "Titulo": Lembrete.query.get(id).titulo,
            "Mensagem": Lembrete.query.get(id).mensagem,
            "Criacao": Lembrete.quey.get(id).criacao,
            "Visualizacao": Lembrete.query.get(id).visualizacao
        }
        
    def listaAll():
        lembretes = Lembrete.query.all()
        resultado = []
        for lembrete in lembretes:
            resultado.append({
                "IdLembrete": lembrete.id,
                "DestinatarioId": lembrete.destinatarioId,
                "DestinatarioCargo": lembrete.destinarioCargo,
                "Titulo": lembrete.titulo,
                "Mensagem": lembrete.mensagem,
                "Criacao": lembrete.criacao,
                "Visualizacao": lembrete.visualizacao
            })
        return jsonify(resultado)
    
    def update(id, lembrete):
        old_lembrete = Lembrete.query.get(id)
        
        old_lembrete.destinatarioCargo = lembrete.destinatarioCargo
        old_lembrete.titulo = lembrete.titulo
        old_lembrete.mensagem = lembrete.mensagem
        old_lembrete.visualizacao = lembrete.visualizacao
        MainRepository.db.session.merge(old_lembrete)
        MainRepository.db.session.commit()
        
        return f"Lembrete ID {id} atualizado."
    
    def delete(id):
        lembrete = Lembrete.query.get(id)
        
        MainRepository.db.session.delete(lembrete)
        MainRepository.db.session.commit()
        
        return f"Lembrete ID {id} deletado."
    
    def create(Lembrete):
        MainRepository.db.session.add(Lembrete)
        MainRepository.db.session.commit()
        
        return f"Lembrete ID {Lembrete.idLembrete} criado."