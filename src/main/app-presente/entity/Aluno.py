from entity.Turma import Turma
from entity.CursoEnum import Curso
from repository.MainRepository import MainRepository


    
class Aluno(MainRepository.db.Model):
    #__tablename__ = 'alunos'
    id = MainRepository.db.Column(MainRepository.db.Integer, primary_key=True)
    ativo = MainRepository.db.Column(MainRepository.db.Boolean, nullable=False)
    nome = MainRepository.db.Column(MainRepository.db.String, nullable=False)
    ra = MainRepository.db.Column(MainRepository.db.Integer, nullable=False, unique=True)
    turma_id = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('turma.id'))
    curso = MainRepository.db.Column(MainRepository.db.Enum(Curso))
    presenca = MainRepository.db.relationship('presenca', backref='aluno')

    

    def __init__(self, id:int, ativo:bool,nome:str, RA:int, turma:Turma, curso:Curso):
        self._id = id
        self._ativo = ativo
        self._nome = nome
        self._RA = RA
        self._turma = turma
        self._curso = curso
        


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
        
            
            

    



