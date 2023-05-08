#! /bin/python3

# Essa classe é um controller no banco de dados, basta chamar o metodo execute() para efetuar a query
#   TO DO: Localizar e tratar exceções

import psycopg2 as database


class Conexao():

    controle = ""
    databaseName = ""

    def __init__(self, databaseName):
        self.databaseName = databaseName

    def estabelecerConexao():
        try:
            dadosConexao = database.connect(
                host="localhost",
                database= self.databaseName,
                user="postgres",
                password="postgree"
            )
            self.controle = dadosConexao.cursor()
        except database.Error as e:
            print(f"Não foi possivel realizar a conexão, Exception:{e}")
            exit(1)


# Encerrando conexão 

    def encerrarConexao():
        self.controle.close()