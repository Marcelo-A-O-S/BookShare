import mysql.connector
from typing import TypeVar, Generic, Any, List
T = TypeVar("T");
conexao = mysql.connector.connect(
    host='localhost',    # Endereço do servidor MySQL
    user='root',  # Nome de usuário
    password='123456',# Senha
    database='sa4'  # Nome do banco de dados
    )
cursor = conexao.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuario (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(50),
        idade INT
    )
''')
class Connection:
    def Insert(value : T) -> T:
        valores = [];
        campos = [];
        tabela = value.__class__.__name__.lower();
        colunas = ""
        values = ""
        propriedades = [propriedade for propriedade in vars(value)];
        for prop in propriedades:
            campos.append(prop);
            value_param = getattr(value, prop)
            print(type(value_param))
            if type(value_param) == str:
                valores.append("'"+value_param+"'");
            elif type(value_param) == int:
                valores.append(value_param)


        for i in range(len(campos)):
            colunas += "{},".format(campos[i]);
            values += "{},".format(valores[i]);
        query = "insert into {} ({}) values({});".format(tabela,colunas.rstrip(colunas[-1]),values.rstrip(values[-1]));
        print(query)
        cursor.execute(query);
        conexao.commit()
        conexao.close()
        return value

    def List(value: T ) -> T:
        ListGeneric : List[T] = []
        tabela = value.__class__.__name__.lower();
        query = "select * from {};".format(tabela)
        cursor.execute(query);
        resultado = cursor.fetchall();
        propriedades =  [propriedade for propriedade in vars(value)]

