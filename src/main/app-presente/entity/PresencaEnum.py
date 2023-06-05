from enum import Enum

class TipoPresenca(Enum):
    Normal = 'NORMAL'
    Manual = 'MANUAL'

#Para acessar o valor do enum Presenca.tipoEscolhido.value
#Ex: Presenca.Normal.value 
#Output: Normal
#adaptar para sql_alchemy