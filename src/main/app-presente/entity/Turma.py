from repository.MainRepository import MainRepository

class Turma(MainRepository.db.Model):

    #__tablename__ ='turmas'
    
    id = MainRepository.db.Column(MainRepository.db.Integer, primary_key=True)
    ativo = MainRepository.db.Column(MainRepository.db.Boolean, nullable=False)
    nome = MainRepository.db.Column(MainRepository.db.String(50), nullable=False)
    ano = MainRepository.db.Column(MainRepository.db.Integer, nullable=False)
    semestre = MainRepository.db.Column(MainRepository.db.String(1), nullable=False)
    chamada = MainRepository.db.relationship('chamada', backref='turma')
    presenca = MainRepository.db.relationship('presenca', backref='turma')

  


    
