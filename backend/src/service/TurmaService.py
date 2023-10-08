from entity.Turma import Turma
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
    def post_turma(turma_dto):
        
        turma = TurmaService.to_entity(turma_dto)

        assert turma.nome != 'NOT_FOUND', "Campo 'nome' inexistente."
        assert turma.ano != 'NOT_FOUND', "Campo 'ano' inexistente."
        assert turma.semestre != 'NOT_FOUND', "Campo 'semestre' inexistente."
        assert turma.turno != 'NOT_FOUND', "Campo 'turno' inexistente."
        assert turma.modalidade != 'NOT_FOUND', "Campo 'modadelidade' inexistente."
        assert turma.curso != 'NOT_FOUND', "Campo 'curso' inexistente."

        assert len(turma.nome) > 3, "Nome com tamanho inválido."
        assert turma.nome.isalpha(), "O nome deve conter apenas letras."
        

        assert 2000 <= int(turma.ano) <= 2023, "Ano inválido."
        assert 1 <= int(turma.semestre) <= 8, "Semestre inválido."


        return TurmaRepository.register(Turma(status=turma.status, nome=turma.nome, ano=turma.ano, semestre=turma.semestre, turno=turma.turno, modalidade=turma.modalidade, curso=turma.curso))
    
    @staticmethod
    def update(id, turma_dto):
        
        turma = TurmaService.to_entity(turma_dto)

        assert turma.nome != 'NOT_FOUND', "Campo 'nome' inexistente."
        assert turma.ano != 'NOT_FOUND', "Campo 'ano' inexistente."
        assert turma.semestre != 'NOT_FOUND', "Campo 'semestre' inexistente."
        assert turma.turno != 'NOT_FOUND', "Campo 'turno' inexistente."
        assert turma.modalidade != 'NOT_FOUND', "Campo 'modadelidade' inexistente."
        assert turma.curso != 'NOT_FOUND', "Campo 'curso' inexistente."

        assert len(turma.nome) > 3, "Nome com tamanho inválido."
        assert turma.nome.isalpha(), "O nome deve conter apenas letras."
        

        assert 2000 <= int(turma.ano) <= 2023, "Ano inválido."
        assert 1 <= int(turma.semestre) <= 8, "Semestre inválido."
        
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