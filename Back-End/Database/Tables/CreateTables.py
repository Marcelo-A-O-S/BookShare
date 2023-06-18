from Database.Connection.Conn import Connection
def CreateUsuario():
    conn = Connection();
    conexao = conn.Conexao();
    cursor = conn.Cursor(conexao);
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuario
        (
        id int primary Key auto_increment not null,
        primeironome varchar(50) not null,
        ultimonome varchar(50) not null,
        email varchar(60) not null,
        papelAtribuido varchar(15) not null,
        senhaHash varchar(255) not null,
        senhaSalt varchar(255) not null
        )
    ''');
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS livro
        (
        id int primary Key auto_increment not null,
        nome varchar(80) not null,
        descricao varchar(50) not null,
        livro varchar(500) not null
        )
    ''');
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS post
        (
        id int primary Key auto_increment not null,
        idUsuario int not null,
        idLivro int not null,
        foreign key(idUsuario) references sa4.usuario(id) on update cascade on delete cascade,
        foreign key(idLivro) references sa4.livro(id) on update cascade on delete cascade
        )
    ''');
    conexao.commit();
    cursor.close();
    conexao.close();
def CreateLivro():
    conn = Connection();
    conexao = conn.Conexao();
    cursor = conn.Cursor(conexao);
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS livro
        (
        id int primary Key auto_increment not null,
        nome varchar(80) not null,
        descricao varchar(50) not null,
        livro varchar(500) not null
        )
    ''')
    conexao.commit();
    cursor.close();
    conexao.close();
def CreatePost():
    conn = Connection();
    conexao = conn.Conexao();
    cursor = conn.Cursor(conexao);
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS post
        (
        id int primary Key auto_increment not null,
        idUsuario int not null,
        idLivro int not null,
        foreign key(idUsuario) references sa4.usuario(id) on update cascade on delete cascade,
        foreign key(idLivro) references sa4.livro(id) on update cascade on delete cascade
        )
    ''')
    conexao.commit();
    cursor.close();
    conexao.close();
