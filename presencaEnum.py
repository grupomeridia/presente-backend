from enum import Enum

class Presenca(Enum):
    Normal = 'NORMAL'
    Manual = 'MANUAL'

#Para acessar o valor do enum Presenca.tipoEscolhido.value
#Ex: Presenca.Normal.value 
#Output: Normal