from enum import Enum

class Curso(Enum):

    Engenharia_de_software = 'Engenharia de Software'
    Analise_e_desenvolvimento_de_sistemas = 'Análise e Desenvolvimento de Sistemas'

#Para acessar o valor do enum Curso.tipoEscolhido.value
#Ex: Curso.engenharia.value 
#Output: ENGENHARIA DE SOFTWARE