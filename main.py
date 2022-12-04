#! /bin/python3

from dependencias import *


## Objetos LED & RFID522
red = LED(22)
green = LED(23)
blue = LED(24)

reader = SimpleMFRC522()

## Banco de dados
dadosConexao={
	"user":"root",
	"password":"dovah",
	"host":"localhost",
	"port":3306,
	"database":"chamada"
}

conexao = database.connect(**dadosConexao)
cursor = conexao.cursor()

cursor.execute("SELECT * FROM alunos;")
numeroAlunos = len(cursor.fetchall())

cursor.execute("SELECT TagID FROM alunos;") #Enviar comando para database
alunos = cursor.fetchall()		 #Receber retorno do comando
naoEncontrado = True

#Função que irá verificar se o aluno já não registrou presença quando ele aproximar o crachá
def coletaAlunos():
	dataAtual = datetime.now()
	dataAtual = str(dataAtual.strftime("%Y-%m-%d"))
	cursor.execute(f"SELECT Data FROM registroSetembro WHERE Data LIKE '%{dataAtual}%';")
	alunosPresentes = len(cursor.fetchall())
	cursor.execute(f"SELECT Nome,RA,Data FROM registroSetembro WHERE Data LIKE '%{dataAtual}%';")
	dados = cursor.fetchall()
	listaAlunos = []

	for x in range(alunosPresentes):
			myDict = {"ID":x+1, "nome":dados[x][0], "RA":dados[x][1], "horario":dados[x][2].strftime('%Y-%m-%d %H:%M:%S')}
			listaAlunos.append(myDict)

	return listaAlunos


def verificaPresenca(nomeAtual,RA) -> None:
	verificaAluno = True
	dataAtual = datetime.now()
	dataAtual = str(dataAtual.strftime("%Y-%m-%d"))	
	cursor.execute(f"SELECT Data FROM registroSetembro WHERE RA={RA};")
	dataAtualDB = cursor.fetchall()
	for x in range(entradasAnteriores):
		dataLista = dataAtualDB[x] 
		dataSimples = str(dataLista[0])
		if(dataAtual in dataSimples):
			red.on()
			blue.on()
			green.on()
			return False
	if(verificaAluno):
		return True

#Função que irá registrar a presença somente após a verificação da função "verificaPresenca"


def registraPresenca(aut,nomeAtual,RA) -> None:
		if(aut):
			horarioAtual = datetime.now()
			horarioAtual = horarioAtual.strftime("%Y-%m-%d %H:%M:%S")
			print(f"Inserindo presença neste horário {horarioAtual}")
			cursor.execute(f"INSERT INTO registroSetembro (Data, Nome, RA, Presenca) VALUES('{horarioAtual}','{nomeAtual}', {RA}, True);")
			conexao.commit()
			print("Presença OK")

			red.off()
			blue.off()
			green.on()


#Iniciando loop principal

try:
	while(True):
		naoEncontrado = True
		red.off()
		green.off()
		blue.on()
		
		idCracha,_ = reader.read()
		
		conexao = database.connect(**dadosConexao)
		cursor = conexao.cursor()

		
		for x in range(numeroAlunos):
			if idCracha in alunos[x]:			#Validando ID
				cursor.execute(f"SELECT nome FROM alunos WHERE TagID = {idCracha};") #Nome do aluno dono do crachá
				nomeAtual = cursor.fetchone()
				nomeAtual = str(nomeAtual[0])

				cursor.execute(f"SELECT RA FROM alunos WHERE TagID = {idCracha};")  #RA do aluno dono do crachá 
				RA = cursor.fetchone()
				RA = RA[0]

				cursor.execute(f"SELECT Data FROM registroSetembro WHERE RA={RA};") #Solicitando o numero de datas com presenças já registradas deste aluno
				entradasAnteriores = len(cursor.fetchall())

				naoEncontrado = False

				registraPresenca(verificaPresenca(nomeAtual,RA),nomeAtual,RA)	    #Verificando duplicidade de presença e registrando presença diaria
				sleep(2)							    #Delay para poder exibir LED antes de apagar 
				break;
			else:
				continue;

		if(naoEncontrado):								    #Ligando LED vermelha caso crachá seja inválido
			green.off()
			blue.off()
			red.on()
			sleep(2)		
	green.off()										    #Apagando todos LEDs para evitar BUGs
	red.off()
	blue.off()

	
except KeyboardInterrupt:										
	print("Encerrando o programa!")
			

cursor.close()
conexao.close()
