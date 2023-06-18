from Database.Connection.Conn import Connection
from typing import TypeVar
import mysql.connector
T = TypeVar("T")

class LivroCustomServices:
    def __init__(self) -> None:
        pass

    def VerificarSeExisteBook(self, value):
        try:
            conn = Connection();
            conexao = conn.Conexao();
            cursor = conn.Cursor(conexao);
            query = "select count(*) as retorno from livro livro where livro.nome = '{}';".format(value);
            cursor.execute(query);
            result = cursor.fetchall();
            for valor in result:
                return valor['retorno']

        except mysql.connector.Error as Err:
            return Err.msg;
    def BuscarLivroPorNome(self, value: T, nome ):
        try:
            conn = Connection();
            conexao = conn.Conexao();
            cursor = conn.Cursor(conexao);
            query = "select * from livro livro where livro.nome = '{}';".format(nome);
            cursor.execute(query);
            result = cursor.fetchall();
            propriedades =  [propriedade for propriedade in vars(value)]
            for linha in result:
                for prop in propriedades:
                    setattr(value, prop, linha[prop])
            return value
        except mysql.connector.Error as Err:
            return Err.msg;
