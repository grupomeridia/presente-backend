from entity.TurnoEnum import Turno
from entity.ModalidadeEnum import Modalidade
from entity.CursoEnum import Curso
class TurmaDTO:
    def __init__(self, status:bool, nome:str, ano:int, semestre:int, turno:Turno, modalidade:Modalidade, curso:Curso):
        self.stauts = status
        self.nome = nome
        self.ano = ano
        self.semestre = semestre
        self.turno = turno
        self.modalidade = modalidade
        self.curso = curso