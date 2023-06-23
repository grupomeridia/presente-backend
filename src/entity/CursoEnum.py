from enum import Enum

class Curso(Enum):
    engenharia_software = 'ENGENHARIA DE SOFTWARE'
    ads = 'ANALISE E DESENVOLVIMENTO DE SISTEMAS'

#Para acessar o valor do enum Curso.tipoEscolhido.value
#Ex: Curso.engenharia.value 
#Output: ENGENHARIA DE SOFTWARE