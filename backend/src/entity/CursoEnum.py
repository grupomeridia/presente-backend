from enum import Enum

class Curso(Enum):
    ENGENHARIA_DE_SOFTWARE = 'ENGENHARIA_DE_SOFTWARE'
    ANALISE_E_DESENVOLVIMENTO_DE_SISTEMAS = 'ANALISE_E_DESENVOLVIMENTO_DE_SISTEMAS'

#Para acessar o valor do enum Curso.tipoEscolhido.value
#Ex: Curso.engenharia.value 
#Output: ENGENHARIA DE SOFTWARE