
#! /bin/python3

import mariadb as database
from datetime import datetime


def coletaAlunos():
		
	dadosConexao={
		"user":"root",
		"password":"dovah",
		"host":"localhost",
		"port":3306,
		"database":"chamada"
	}

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


