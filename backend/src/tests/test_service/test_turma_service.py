from service.TurmaService import TurmaService

class test_turma_service():
    def test_deve_retornar_uma_turma():
        
        data = TurmaService.getTurma(id)
        assert all(key in data for key in ["Ano", "Id", "Semestre", "curso", "modalidade", "nome", "status", "turno"])