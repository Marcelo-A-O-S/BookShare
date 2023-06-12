from Database.Connection.Conn import Connection
import mysql.connector

class UserCustomServices:
    def __init__(self) -> None:
        pass
    def VerificarExisteEmailUsuario(self, email:str ) -> str:
        try:
            conn = Connection();
            conexao = conn.Conexao();
            cursor = conn.Cursor(conexao);
            query = "select case when count(*) > 0 then 'true' else 'false' end as resultado from usuario  _user where _user.email = '{}'".format(email);
            cursor.execute(query)
            resultado = cursor.fetchall()
            cursor.close()
            conexao.close()
            for valor in resultado:
                if valor['resultado'] == 'false':
                    return False;
                else:
                    return True;
        except mysql.connector.Error as Err:
            return Err.msg;


    def BuscarPorEmailUsuario(self, email:str):
        try:
            conn = Connection();
            conexao = conn.Conexao();
            cursor = conn.Cursor(conexao);
            query = "select * from usuario _user where _user.email = '{}' limit 1".format(email);
            cursor.execute(query)
            resultado = cursor.fetchall()
            cursor.close()
            conexao.close()
            return resultado
        except mysql.connector.Error as Err:
            return Err.msg;
