from Database.Connection.Conn import Connection
from typing import TypeVar, Generic, Any, List
import mysql.connector
import mysql.connector.errors
T = TypeVar("T");

class BaseGeneric():
    def __init__(self) -> T:
        super().__init__()
    def Insert(self,value : T) -> T:
        try:
            conn = Connection()
            conexao = conn.Conexao()
            cursor = conn.Cursor(conexao)
            valores = [];
            campos = [];
            tabela = value.__class__.__name__.lower();
            colunas = ""
            values = ""
            propriedades = [propriedade for propriedade in vars(value)];
            for prop in propriedades:
                campos.append(prop);
                value_param = getattr(value, prop)
                if type(value_param) == str:
                    valores.append('"{}"'.format(value_param));
                elif type(value_param) == int:
                    valores.append(value_param)
                elif type(value_param) == bytes:
                    valor_byte = value_param.hex()
                    valores.append('"{}"'.format(valor_byte))
            for i in range(len(campos)):
                colunas += "{},".format(campos[i]);
                if type(valores[i]) == str:
                    string: str = valores[i]
                    values += '{}'.format(string)
                    values += ",";
                else:
                    values += "{},".format(valores[i]);
            query = "insert into {} ({}) values({});".format(tabela,colunas.rstrip(colunas[-1]),values.rstrip(values[-1]));
            cursor.execute(query);
            conexao.commit()
            conexao.close()
            return "Inserido no banco com sucesso!"
        except mysql.connector.Error as e:
            print("Erro no banco de dados:", e.msg)

    def List(self, value: T) -> List[T]:
        try:
            conn = Connection()
            conexao = conn.Conexao()
            cursor = conn.Cursor(conexao)
            ListGeneric : List[T] = []
            tabela = value.__class__.__name__.lower();
            query = "select * from {};".format(tabela);
            cursor.execute(query);
            lista = cursor.fetchall()
            cursor.close();
            conexao.close();
            propriedades =  [propriedade for propriedade in vars(value)]
            for linha in lista:
                for prop in propriedades:
                    setattr(value, prop, linha[prop])
                ListGeneric.append(value)

            return ListGeneric

        except mysql.connector.Error as err:
            print("Erro no banco de dados:", err.msg)

    def Update(self,value: T) -> T:
        try:
            conn = Connection()
            conexao = conn.Conexao()
            cursor = conn.Cursor(conexao)
            colunas = [];
            valores = [];
            tabela = value.__class__.__name__.lower();
            referencia = ""
            identificador = "";
            valor_identificador = "";
            corpo = ""
            propriedades = [propriedade for propriedade in vars(value)];
            for prop in propriedades:
                if prop.lower() == 'id':
                    identificador = prop;
                    valor_identificador = getattr(value, prop);
                else:
                    colunas.append(prop);
                    value_param = getattr(value, prop);
                    if type(value_param) == str:
                        valores.append('"{}"'.format(value_param))

            for i in range(colunas.__len__()):
                corpo += ' {} = {},'.format(colunas[i], valores[i])

            referencia = '{} = {}'.format(identificador, valor_identificador)
            query = 'update {} set {} where {}'.format(tabela, corpo.rstrip(corpo[-1]), referencia)
            cursor.execute(query);
            conexao.commit();
            cursor.close();
            conexao.close();
        except mysql.connector.Error as e:
            return e.msg
