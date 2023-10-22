from entity.TurnoEnum import Turno
from entity.ModalidadeEnum import Modalidade
from entity.CursoEnum import Curso
from pydantic import validate_arguments

class TurmaDTO:
    @validate_arguments
    def __init__(self, id_materia:int, status:bool, nome:str, ano:int, semestre:int, turno:Turno, modalidade:Modalidade, curso:Curso):
        self.id_materia = id_materia
        self.status = status
        self.nome = nome
        self.ano = ano
        self.semestre = semestre
        self.turno = turno
        self.modalidade = modalidade
        self.curso = curso