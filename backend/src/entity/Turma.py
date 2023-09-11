from entity.TurnoEnum import Turno
from entity.ModalidadeEnum import Modalidade
from entity.CursoEnum import Curso
from repository.MainRepository import MainRepository


class Turma(MainRepository.db.Model):
    __tablename__ = 'turmas'
    idTurma = MainRepository.db.Column(MainRepository.db.Integer, primary_key=True)
    status = MainRepository.db.Column(MainRepository.db.Boolean, nullable=False)
    nome = MainRepository.db.Column(MainRepository.db.String(50), nullable=False)
    ano = MainRepository.db.Column(MainRepository.db.Integer, nullable=False)
    semestre = MainRepository.db.Column(MainRepository.db.Integer, nullable=False)
    turno = MainRepository.db.Column(MainRepository.db.Enum(Turno))
    modalidade = MainRepository.db.Column(MainRepository.db.Enum(Modalidade))
    curso = MainRepository.db.Column(MainRepository.db.Enum(Curso))
    chamadas = MainRepository.db.relationship('Chamada', back_populates='turma')
    alunos = MainRepository.db.relationship('Aluno', secondary='turma_aluno')
    professores = MainRepository.db.relationship('Professor', secondary='turma_professor')

    def __init__(self, ativo:bool, nome:str, ano:int, semestre:int):
        self.ativo = ativo
        self.nome = nome
        self.ano = ano
        self.semestre = semestre

  


    
