# Setup

```
cd deployment
docker-compose up
SET autocommit=0;
SET GLOBAL innodb_status_output=ON;
SET GLOBAL innodb_status_output_locks=ON;
```

## Init

`cd ../scripts`
`execute run.sql`

```
drop table accounts;
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
```

# Read uncommitted

## T1

```
start transaction ;

select * from accounts;

insert into accounts (login, balance, created_at) values  ('ivan', 750, now());
delete from accounts where login = 'mark';

update accounts set balance = 1500 where login = 'mykyta';

rollback ;
```

## T2

```
start transaction ;

select * from accounts;

select sum(balance) from accounts;
```

T2 see uncommitted data and could do wrong logic. After T1 rollback T2 sum will be changed.

#Read committed

##T1

```
start transaction ;

select * from accounts;

insert into accounts (login, balance, created_at) values  ('ivan', 750, now());
delete from accounts where login = 'mark';

update accounts set balance = 1500 where login = 'mykyta';

select * from accounts;

select sum(balance) from accounts;

commit;
```

## T2

```
start transaction ;

select * from accounts;

select sum(balance) from accounts;

T2 doesn't see uncommitted data, after commit T2 see new data. T1 sees his local data.
```

# Repeatable read

## T1

```
start transaction ;

select * from accounts;

insert into accounts (login, balance, created_at) values  ('ivan', 750, now());
update accounts set balance = 1500 where login = 'mark';
delete from accounts where login = 'mykyta';

select * from accounts;

select sum(balance) from accounts;

commit;
```

## T2

```
start transaction ;

select * from accounts;

update accounts set balance = 2000 where login = 'mark';
select sum(balance) from accounts;

commit ;
```

T2 will wait until T2 commits or rollback changes.

Mysql doesn't have reading phantoms
