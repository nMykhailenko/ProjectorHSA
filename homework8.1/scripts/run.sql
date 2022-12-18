create table if not exists accounts
(
	id int unsigned auto_increment primary key,
	login varchar(255) not null,
	balance bigint default 0 not null,
	created_at timestamp default now()
) collate=utf8mb4_unicode_ci;

insert into accounts (login, balance) values ('mykyta', 150);
insert into accounts (login, balance) values ('mark', 300);
insert into accounts (login, balance) values ('illia', 450);

