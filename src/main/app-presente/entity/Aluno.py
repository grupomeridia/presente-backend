#! /bin/python3

#from entity.PresencaEnum import Presenca
from entity.Turma import Turma
from entity.CursoEnum import Curso
from repository.AlunoRepository import AlunoRepository

#Primeiro ID - Vamos melhorar isso em breve.

    
class Aluno(AlunoRepository.db.Model):
    __tablename__ = 'alunos'
    id = AlunoRepository.db.Column(AlunoRepository.db.Integer, primary_key=True)
    ativo = AlunoRepository.db.Column(AlunoRepository.db.Boolean, nullable=False)
    nome = AlunoRepository.db.Column(AlunoRepository.db.String, nullable=False)
    ra = AlunoRepository.db.Column(AlunoRepository.db.Integer, nullable=False, unique=True)
    turma_id = AlunoRepository.db.Column(AlunoRepository.db.Integer, AlunoRepository.db.ForeignKey('turmas.id'))
    curso = AlunoRepository.db.Column(AlunoRepository.db.Enum(Curso))
    presenca = AlunoRepository.db.relationship('presencas', backref='alunos')

    #Construtor

    def __init__(self, id:int, ativo:bool,nome:str, RA:int, turma:Turma, curso:Curso):
        self._id = id
        self._ativo = ativo
        self._nome = nome
        self._RA = RA
        self._turma = turma
        self._curso = curso
        


    #Validações

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        if(isinstance(value, int) and value > 0):
            self._id = value
        else:
            raise ValueError("ID incorreto, deve ser um número maior que zero")

    @id.deleter
    def id(self):
        self._id = None

    @property
    def RA(self):
        return self._RA

    @RA.setter
    def RA(self, value):
        if isinstance(value, int) and value > 50000:
            # Criar validação aqui para verificar se o RA inserido já existe no banco de dados, IMPEDITIVO: Falta criar a classe controller. 
            self._RA = value
        else:
            raise Exception("RA inválido!")
        
    @RA.deleter
    def RA(self):
        self._RA = None


    ### Métodos
    
    def verificaRA(self, ra) -> bool:
        #IMPEDITIVO: Falta criar a classe controller
        pass

    def verificaPresenca(self, ra) -> bool:
        #IMPEDITIVO: Falta criar a classe controller
        pass

    def registrarPresenca(self, ra):
        if self.verificaRA() and self.verificaPresenca():
                #IMPEDITIVO: Falta criar a classe controller 
                #Registrar presenca aqui
                pass
        else:
        
            raise Exception("Aluno já realizou presença!")
        
            
            

    



