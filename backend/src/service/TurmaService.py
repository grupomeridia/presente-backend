
from entity.CursoEnum import Curso
from entity.TurnoEnum import Turno
from entity.ModalidadeEnum import Modalidade
from entity.Turma import Turma
from entity.Aluno import Aluno
from entity.Professor import Professor
from entity.Materia import Materia
from dtos.TurmaDTO import TurmaDTO

from repository.TurmaRepository import TurmaRepository

import re

class TurmaService():
    @staticmethod
    def get_turma(id):
        assert id != None, "Nenhum ID enviado."
        assert int(id) if isinstance(id, (int, str)) and id.isdigit() else None, "ID incorreto."
        assert int(id) > 0 and int(id) < 999999, "ID inválido"
        assert Turma.query.get(id) != None, f"Nenhuma turma com o ID {id} foi encontrada."
        
        return TurmaRepository.get_turma_by_id(id)
    
    @staticmethod
    def post_turma(status, id_materia, nome, ano, semestre, turno, modalidade, curso):      

        modalidades = [x.value for x in Modalidade]
        turnos = [x.value for x in Turno]
        cursos = [x.value for x in Curso]

        assert modalidade in modalidades, "Modalidade inválida"
        assert turno in turnos, "Turno inválido"
        assert curso in cursos, "Curso inválido"
        assert id_materia != 'NOT_FOUND', "Campo 'id_materia' inexistente."


        assert nome != 'NOT_FOUND', "Campo 'nome' inexistente."
        assert ano != 'NOT_FOUND', "Campo 'ano' inexistente."
        assert semestre != 'NOT_FOUND', "Campo 'semestre' inexistente."
        assert turno != 'NOT_FOUND', "Campo 'turno' inexistente."
        assert modalidade != 'NOT_FOUND', "Campo 'modadelidade' inexistente."
        assert curso != 'NOT_FOUND', "Campo 'curso' inexistente."

        assert int(id_materia) if isinstance(id_materia, (int,str)) and str(id_materia).isdigit() else None, "ID de matéria incorreto."
        assert int(id_materia) > 0 and int(id_materia) < 999999, "ID de matéria inválido."
        assert re.match(r'^\d+$', str(id_materia)), "O ID de matéria deve ter apenas números."
        materia = Materia.query.get(id_materia)
        assert materia is not None, "Matéria não encontrada"

        assert len(nome) > 3, "Nome com tamanho inválido."
        assert nome.isalpha(), "O nome deve conter apenas letras."
        

        assert 2000 <= int(ano) <= 2023, "Ano inválido."
        assert 1 <= int(semestre) <= 8, "Semestre inválido."

        turma = TurmaService.to_entity(TurmaDTO(status=status, id_materia=id_materia, nome=nome, ano=ano, semestre=semestre, turno=turno, modalidade=modalidade, curso=curso))
        return TurmaRepository.register(turma)
    
    @staticmethod
    def update(id_turma, status, id_materia,nome, ano, semestre, turno, modalidade, curso):
        
        modalidades = [x.value for x in Modalidade]
        turnos = [x.value for x in Turno]
        cursos = [x.value for x in Curso]

        assert modalidade in modalidades, "Modalidade inválida"
        assert turno in turnos, "Turno inválido"
        assert curso in cursos, "Curso inválido"
        
        assert int(id_turma) if isinstance(id_turma, (int, str)) and id_turma.isdigit() else None, "ID incorreto."
        assert int(id_turma) > 0 and int(id_turma) < 999999, "ID inválido"

        assert id_materia != 'NOT_FOUND', "Campo 'id_materia' inexistente."
        assert nome != 'NOT_FOUND', "Campo 'nome' inexistente."
        assert ano != 'NOT_FOUND', "Campo 'ano' inexistente."
        assert semestre != 'NOT_FOUND', "Campo 'semestre' inexistente."
        assert turno != 'NOT_FOUND', "Campo 'turno' inexistente."
        assert modalidade != 'NOT_FOUND', "Campo 'modadelidade' inexistente."
        assert curso != 'NOT_FOUND', "Campo 'curso' inexistente."
        
        assert int(id_materia) if isinstance(id_materia, (int,str)) and str(id_materia).isdigit() else None, "ID de matéria incorreto."
        assert int(id_materia) > 0 and int(id_materia) < 999999, "ID de matéria inválido."
        assert re.match(r'^\d+$', str(id_materia)), "O ID de matéria deve ter apenas números."

        assert len(nome) > 3, "Nome com tamanho inválido."
        assert nome.isalpha(), "O nome deve conter apenas letras."

        assert 2000 <= int(ano) <= 2023, "Ano inválido."
        assert 1 <= int(semestre) <= 8, "Semestre inválido."
        
        turma = TurmaService.to_entity(TurmaDTO(status=status, id_materia=id_materia,nome=nome, ano=ano, semestre=semestre, turno=turno, modalidade=modalidade, curso=curso))
        return TurmaRepository.update(id_turma, turma)
    
    @staticmethod
    def delete(id):
        assert int(id) if isinstance(id, (int, str)) and id.isdigit() else None, "ID incorreto."
        assert int(id) > 0 and int(id) < 999999, "ID inválido"
        assert Turma.query.get(id) != None, f"Nenhuma turma com o ID {id} foi encontrada."
        assert Turma.query.filter(Turma.id_turma == id).first() is not None, "Turma não encontrada"
        return TurmaRepository.delete(id)
    
    @staticmethod
    def cadastrar_aluno(id_turma, id_aluno):
        
        assert int(id_aluno) if isinstance(id_aluno, (int)) else None, "Aluno id incorreto."
        assert int(id_turma) if isinstance(id_turma, (int)) else None, "Turma id incorreto."
        assert int(id_aluno) > 0 and int(id_aluno) < 999999, "ID do aluno inválido"
        assert int(id_turma) > 0 and int(id_turma) < 999999, "ID da turma inválida"
        
        aluno = Aluno.query.get(id_aluno)
        if aluno and Turma.query.get(id_turma) in aluno.turmas:
            return ({'mensagem': 'Aluno ja cadastrado na turma'}), 400

        return TurmaRepository.cadastrar_aluno(id_turma, id_aluno)

    @staticmethod
    def cadastrar_professor(id_turma, id_professor):
        
        assert int(id_professor) if isinstance(id_professor, (int)) else None, "Professor id incorreto."
        assert int(id_turma) if isinstance(id_turma, (int)) else None, "Turma id incorreto."
        assert int(id_professor) > 0 and int(id_professor) < 999999, "ID do professor inválido"
        assert int(id_turma) > 0 and int(id_turma) < 999999, "ID da turma inválida"

        professor = Professor.query.get(id_professor)
        if professor and Turma.query.get(id_turma) in professor.turmas:
            return ({'mensagem': 'Professor ja cadastrado na turma'}), 400

        return TurmaRepository.cadastrar_professor(id_turma, id_professor)

    @staticmethod
    def to_entity(turma_dto):
        turma = Turma(status=turma_dto.status, id_materia=turma_dto.id_materia, nome=turma_dto.nome, ano=turma_dto.ano, semestre=turma_dto.semestre, turno=turma_dto.turno, modalidade=turma_dto.modalidade, curso=turma_dto.curso)

        return turma