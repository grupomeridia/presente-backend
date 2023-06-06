from entity.Aluno import Aluno
from repository.AlunoRepository import AlunoRepository
from repository.MainRepository import MainRepository

AlunoRepository.criarTabela(MainRepository.app, MainRepository.db)


print("eca")
