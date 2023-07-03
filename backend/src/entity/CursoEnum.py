from enum import Enum

class Curso(Enum):
    ENGENHARIA_DE_SOFTWARE = 'Engenharia de Software'
    ANALISE_E_DESENVOLVIMENTO_DE_SISTEMAS = 'Análise e Desenvolvimento de Sistemas'

#Para acessar o valor do enum Curso.tipoEscolhido.value
#Ex: Curso.engenharia.value 
#Output: ENGENHARIA DE SOFTWARE