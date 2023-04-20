
#! /bin/python3

import psycopg2 as database
from datetime import datetime


def coletaAlunos():

	#Conexão com a bd do Postgress

	try:
		dadosConexao = database.connect(
			host="localhost",
			database="chamada_db",
			user="postgres",
			password="postgree"
		)
		cur = dadosConexao.cursor()
		cur.execute("SELECT 1")
		print("Conexao bem sucedida")
	except database.Error as e:
		print("Falha ",e)
	finally:
		cur.close()
		dadosConexao.close()



""""
	Fizemos a mudança de conexão de maribd para postgress,
	este bloco sera descomentado quando o banco de dados for estructurado,
	o codigo não esta funcional precisara particalmente refatorado.

	conexao = database.connect(**dadosConexao)
	cursor = conexao.cursor()
	
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
"""




