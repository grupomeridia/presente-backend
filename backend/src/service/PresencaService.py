from repository.PresencaRepository import PresencaRepository

from entity.Presenca import Presenca
from entity.Chamada import Chamada
from entity.Aluno import Aluno
from entity.CargoEnum import Cargo
from dtos.PresencaDTO import PresencaDTO
from entity.PresencaEnum import TipoPresenca
from datetime import datetime

import re

class PresencaService():
    @staticmethod
    def get_by_id(id):
        assert id != None, "Nenhum ID enviado."
        assert int(id) if isinstance(id, (int,str)) and id.isdigit() else None, "ID incorreto."
        assert int(id) > 0 and int(id) < 999999, "ID inválido."
        assert Presenca.query.get(id) != None, "Nenhua presença com este ID foi encontrado."
        
        return PresencaRepository.get_presenca_by_id(id)

    @staticmethod
    def register(id_aluno, id_chamada, tipo_presenca, horario, status):

        tipoPresenca = [x.value for x in TipoPresenca]

        assert id_aluno != 'NOT_FOUND', "Campo 'id_aluno' inexistente."
        assert id_chamada != 'NOT_FOUND', "Campo 'id_chamada' inexistente."
        assert tipo_presenca != 'NOT_FOUND', "Campo 'tipo_presenca' inexistente."
        
        existe_presenca = Presenca.query.filter_by(id_aluno=id_aluno, id_chamada=id_chamada).first()
        assert existe_presenca is None, "O aluno já possui presença na mesma chamada."
        
        horario = datetime.now().strftime("%d-%m-%Y %H:%M") if horario is None else horario
        assert re.match(r'^\d{2}-\d{2}-\d{4} \d{2}:\d{2}$', horario), "Formato de horário incorreto. Use o formato dd/mm/yyyy HH:MM."

        assert int(id_aluno) if isinstance(id_aluno, (int,str)) and str(id_aluno).isdigit() else None, "ID de aluno incorreto."
        assert int(id_aluno) > 0 and int(id_aluno) < 999999, "ID de aluno inválido."
        assert re.match(r'^\d+$', str(id_aluno)), "O ID de Aluno deve ter apenas números."
        aluno = Aluno.query.get(id_aluno)
        assert aluno is not None, "Aluno não encontrado"

        assert int(id_chamada) if isinstance(id_chamada, (int,str)) and str(id_chamada).isdigit() else None, "ID de chamada incorreto."
        assert int(id_chamada) > 0 and int(id_chamada) < 999999, "ID de chamada inválido."
        assert re.match(r'^\d+$', str(id_chamada)), "O ID de chamada deve ter apenas números."
        chamada = Chamada.query.get(id_chamada)
        assert chamada is not None, "Chamada não encontrada."

        assert tipo_presenca in tipoPresenca, "Tipo de presença incorreto."
        
        assert Chamada.query.filter(Chamada.status == True).first() is not None, "Não existe nenhuma chamada aberta"
        
        presenca = PresencaService.to_entity(PresencaDTO(id_aluno=id_aluno, id_chamada=id_chamada, tipo_presenca=tipo_presenca, horario=horario, status=status, cargo_manual=None, id_manual=None))

        return PresencaRepository.register_presenca(presenca)
    
    @staticmethod
    def marcar_presenca_pelo_ra(ra, cargo_manual, id_manual):

        assert ra != 'NOT_FOUND', "Campo 'RA inexistente."
        assert cargo_manual != 'NOT_FOUND', "Campo 'cargo_manual' inexistente."
        assert id_manual != 'NOT_FOUND', "Campo 'id_manual' inexistente." 

        assert re.match(r'^\d+$', str(ra)), "O RA deve ter apenas números."
        assert ra >= 100000 and ra <= 999999, "RA inválido."

        cargos = [x.value for x in Cargo]
        assert cargo_manual in cargos, "Cargo inválido"

        assert int(id_manual) if isinstance(id_manual, (int)) else None, "Id_manual incorreto."


        return PresencaRepository.marcar_presenca_pelo_ra(ra, cargo_manual, id_manual)
    
    @staticmethod
    def update(id_presenca, id_aluno, id_chamada, tipo_presenca, horario, status):

        tipoPresenca = [x.value for x in TipoPresenca]

        assert id_aluno != 'NOT_FOUND', "Campo 'id_aluno' inexistente."
        assert id_chamada != 'NOT_FOUND', "Campo 'id_chamada' inexistente."
        assert tipo_presenca != 'NOT_FOUND', "Campo 'tipo_presenca' inexistente."
        assert id_presenca != 'NOT_FOUND', "Campo 'id_presenca' inexistente."
        
        horario = datetime.now().strftime("%d-%m-%Y %H:%M") if horario is None else horario
        assert re.match(r'^\d{2}-\d{2}-\d{4} \d{2}:\d{2}$', horario), "Formato de horário incorreto. Use o formato dd/mm/yyyy HH:MM."

        assert int(id_aluno) if isinstance(id_aluno, (int,str)) and str(id_aluno).isdigit() else None, "ID de aluno incorreto."
        assert int(id_aluno) > 0 and int(id_aluno) < 999999, "ID de aluno inválido."
        assert re.match(r'^\d+$', str(id_aluno)), "O ID de Aluno deve ter apenas números."
        aluno = Aluno.query.get(id_aluno)
        assert aluno is not None, "Aluno não encontrado"

        assert int(id_chamada) if isinstance(id_chamada, (int,str)) and str(id_chamada).isdigit() else None, "ID de chamada incorreto."
        assert int(id_chamada) > 0 and int(id_chamada) < 999999, "ID de chamada inválido."
        assert re.match(r'^\d+$', str(id_chamada)), "O ID de chamada deve ter apenas números."
        chamada = Chamada.query.get(id_chamada)
        assert chamada is not None, "Chamada não encontrada."

        assert tipo_presenca in tipoPresenca, "Tipo de presença incorreto."

        assert Chamada.query.filter(Chamada.status == True).first() is not None, "Não existe nenhuma chamada aberta"


        presenca = PresencaService.to_entity(PresencaDTO(id_aluno=id_aluno, id_chamada=id_chamada, tipo_presenca=tipo_presenca, horario=horario, status=status))

        return PresencaRepository.update(id_presenca, presenca)
    
    @staticmethod
    def delete(id):
        assert id != None, "Nenhum ID enviado."
        assert int(id) if isinstance(id, (int,str)) and id.isdigit() else None, "ID incorreto."
        assert int(id) > 0 and int(id) < 999999, "ID inválido."
        assert Presenca.query.get(id) != None, "Nenhua presença com este ID foi encontrado."
        

        return PresencaRepository.delete(id)
    
    @staticmethod
    def to_entity(aluno_dto):
        presenca = Presenca(id_aluno=aluno_dto.id_aluno, id_chamada=aluno_dto.id_chamada, status=aluno_dto.status, tipo_presenca=aluno_dto.tipo_presenca, horario=aluno_dto.horario, cargo_manual=aluno_dto.cargo_manual, id_manual=aluno_dto.id_manual)

        return presenca