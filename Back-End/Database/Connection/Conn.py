import mysql.connector

class Connection:
    def __init__(self):
        pass
    def Conexao(self):
        conexao = mysql.connector.connect(
            host='localhost',    # Endereço do servidor MySQL
            user='root',  # Nome de usuário
            password='123456',# Senha
            database='sa4'  # Nome do banco de dados
            );
        return conexao
    def Cursor(self,conexao):
        cursor = conexao.cursor(dictionary=True);
        return cursor;


