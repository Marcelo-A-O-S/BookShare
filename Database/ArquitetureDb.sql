Create database SA4;

select * from sa4.usuario;
select * from sa4.livro;
use sa4;
create table usuario
(
id int primary Key auto_increment not null,
primeironome varchar(50) not null,
ultimonome varchar(50) not null,
email varchar(60) not null,
papelAtribuido varchar(15) not null,
senhaHash varchar(255) not null,
senhaSalt varchar(255) not null
);
use sa4;
create table livro
(
id int primary Key auto_increment not null,
nome varchar(80) not null,
descricao varchar(50) not null,
livro longtext not null
);

use sa4;
create table post
(
id int primary Key auto_increment not null,
idUsuario int not null,
idLivro int not null,
foreign key(idUsuario) references sa4.usuario(id) on update cascade on delete cascade,
foreign key(idLivro) references sa4.livro(id) on update cascade on delete cascade
);

use sa4;
drop table post;
use sa4;
drop table livro;

select count(*) as retorno from sa4.livro livro where livro.nome = 'Teste';
use sa4;
create table teste(
coluna blob not null 
);
select * from sa4.teste;
insert into sa4.teste (coluna) values ('Teste');
select * from sa4.usuario;

delete from sa4.usuario u where u.id =2;

select * from sa4.usuario _user where _user.email = 'usuarioteste@gmail.com' limit 1;

select case when count(*) > 0 then 'true' else 'false' end as resultado from sa4.usuario  _user where _user.email = "teste" ;
select * from sa4.usuario 