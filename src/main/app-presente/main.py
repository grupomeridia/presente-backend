from entity.Aluno import Aluno
from entity.Chamada import Chamada
from entity.Configuracao import Configuracao
from entity.CursoEnum import Curso
from entity.Presenca import Presenca
from entity.PresencaEnum import TipoPresenca
from entity.Professor import Professor
from entity.Turma import Turma

from repository.MainRepository import MainRepository

with MainRepository.app.app_context():
    MainRepository.db.create_all()

