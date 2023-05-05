from enum import Enum

class Presenca(Enum):
    Normal = 'Normal'
    Manual = 'Manual'

#Para acessar o valor do enum Presenca.tipoEscolhido.value
#Ex: Presenca.Normal.value 
#Output: Normal