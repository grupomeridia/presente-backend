from repository.MateriaRepository import MateriaRepository

from entity.Materia import Materia
from dtos.MateriaDTO import MateriaDTO
import re


class MateriaService():
    @staticmethod
    def get_by_id(id):
        assert id != None, "Nenhum ID enviado."
        assert int(id) if isinstance(id, (int,str)) and id.isdigit() else None, "ID incorreto."
        assert int(id) > 0 and int(id) < 999999, "ID inválido."
        assert Materia.query.get(id) != None, "Nenhuma materia com o este ID foi encontrado"
        
        return MateriaRepository.get_materia_by_id(id)
    
    @staticmethod
    def register(status, nome):

        assert nome != 'NOT_FOUND', "Campo 'nome' inexistente."
        assert re.match("^[a-zA-Z0-9 ]+$", nome), "O nome deve conter apenas letras e números."
        assert 3 <= len(nome) <= 50, "O nome deve ter entre 3 e 50 caracteres."

        assert not Materia.query.filter(Materia.nome == nome).first(), "Matéria ja cadastrada."

        materia = MateriaService.to_entity(MateriaDTO(status=status, nome=nome))

        return MateriaRepository.register(Materia(status=materia.status, nome=materia.nome))
    
    @staticmethod
    def update(id_materia, nome, status):

        assert nome != 'NOT_FOUND', "Campo 'nome' inexistente."
        assert re.match("^[a-zA-Z0-9 ]+$", nome), "O nome deve conter apenas letras e números."
        assert 3 <= len(nome) <= 50, "O nome deve ter entre 3 e 50 caracteres."

        assert not Materia.query.filter(Materia.nome == nome).first(), "Matéria ja cadastrada."
        
        materia = Materia.query.get(id_materia)
        assert materia != None, "Matéria não encontrada."

        materia = MateriaService.to_entity(MateriaDTO(nome=nome, status=status))

        return MateriaRepository.update(id_materia, materia)
    
    @staticmethod
    def delete(id):
        assert id != None, "Nenhum ID enviado."
        assert int(id) if isinstance(id, (int,str)) and id.isdigit() else None, "ID incorreto."
        assert int(id) > 0 and int(id) < 999999, "ID inválido."
        assert Materia.query.get(id) != None, "Nenhuma materia com o este ID foi encontrado"
        
        
        return MateriaRepository.delete(id)
    
    @staticmethod
    def to_entity(materia_dto):
        materia = Materia(status=materia_dto.status, nome=materia_dto.nome)

        return materia