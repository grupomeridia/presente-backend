
from entity.CursoEnum import Curso
from entity.TurnoEnum import Turno
from entity.ModalidadeEnum import Modalidade
from entity.Turma import Turma

from dtos.TurmaDTO import TurmaDTO

from repository.TurmaRepository import TurmaRepository



class TurmaService():
    @staticmethod
    def get_turma(id):
        assert id != None, "Nenhum ID enviado."
        assert int(id) if isinstance(id, (int, str)) and id.isdigit() else None, "ID incorreto."
        assert int(id) > 0 and int(id) < 999999, "ID inválido"
        assert Turma.query.get(id) != None, f"Nenhuma turma com o ID {id} foi encontrada."
        
        return TurmaRepository.get_turma_by_id(id)
    
    @staticmethod
    def post_turma(status, nome, ano, semestre, turno, modalidade, curso):      

        modalidades = [x.value for x in Modalidade]
        turnos = [x.value for x in Turno]
        cursos = [x.value for x in Curso]

        assert modalidade in modalidades, "Modalidade inválida"
        assert turno in turnos, "Turno inválido"
        assert curso in cursos, "Curso inválido"

        assert nome != 'NOT_FOUND', "Campo 'nome' inexistente."
        assert ano != 'NOT_FOUND', "Campo 'ano' inexistente."
        assert semestre != 'NOT_FOUND', "Campo 'semestre' inexistente."
        assert turno != 'NOT_FOUND', "Campo 'turno' inexistente."
        assert modalidade != 'NOT_FOUND', "Campo 'modadelidade' inexistente."
        assert curso != 'NOT_FOUND', "Campo 'curso' inexistente."

        assert len(nome) > 3, "Nome com tamanho inválido."
        assert nome.isalpha(), "O nome deve conter apenas letras."
        

        assert 2000 <= int(ano) <= 2023, "Ano inválido."
        assert 1 <= int(semestre) <= 8, "Semestre inválido."

        turma = TurmaService.to_entity(TurmaDTO(status=status, nome=nome, ano=ano, semestre=semestre, turno=turno, modalidade=modalidade, curso=curso))
        return TurmaRepository.register(turma)
    
    @staticmethod
    def update(id, status, nome, ano, semestre, turno, modalidade, curso):
        
        modalidades = [x.value for x in Modalidade]
        turnos = [x.value for x in Turno]
        cursos = [x.value for x in Curso]

        assert modalidade in modalidades, "Modalidade inválida"
        assert turno in turnos, "Turno inválido"
        assert curso in cursos, "Curso inválido"

        assert int(id) if isinstance(id, (int, str)) and id.isdigit() else None, "ID incorreto."
        assert int(id) > 0 and int(id) < 999999, "ID inválido"

        assert nome != 'NOT_FOUND', "Campo 'nome' inexistente."
        assert ano != 'NOT_FOUND', "Campo 'ano' inexistente."
        assert semestre != 'NOT_FOUND', "Campo 'semestre' inexistente."
        assert turno != 'NOT_FOUND', "Campo 'turno' inexistente."
        assert modalidade != 'NOT_FOUND', "Campo 'modadelidade' inexistente."
        assert curso != 'NOT_FOUND', "Campo 'curso' inexistente."

        assert len(nome) > 3, "Nome com tamanho inválido."
        assert nome.isalpha(), "O nome deve conter apenas letras."

        assert 2000 <= int(ano) <= 2023, "Ano inválido."
        assert 1 <= int(semestre) <= 8, "Semestre inválido."
        
        turma = TurmaService.to_entity(TurmaDTO(status=status, nome=nome, ano=ano, semestre=semestre, turno=turno, modalidade=modalidade, curso=curso))
        return TurmaRepository.update(id, turma)
    
    @staticmethod
    def delete(id):
        assert int(id) if isinstance(id, (int, str)) and id.isdigit() else None, "ID incorreto."
        assert int(id) > 0 and int(id) < 999999, "ID inválido"
        assert Turma.query.get(id) != None, f"Nenhuma turma com o ID {id} foi encontrada."
        assert Turma.query.filter(Turma.id_turma == id).first() is not None, "Turma não encontrada"
        return TurmaRepository.delete(id)
    
    @staticmethod
    def to_entity(turma_dto):
        turma = Turma(status=turma_dto.status, nome=turma_dto.nome, ano=turma_dto.ano, semestre=turma_dto.semestre, turno=turma_dto.turno, modalidade=turma_dto.modalidade, curso=turma_dto.curso)

        return turma