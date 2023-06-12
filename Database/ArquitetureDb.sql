Create database SA4;

use sa4;
drop table usuario;
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