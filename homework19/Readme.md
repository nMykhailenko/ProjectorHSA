## Simple table without partitions

## Table patitioned by shards
### Create table on main shard
```
CREATE TABLE movies (
id bigint not null,
category_id  int not null,
produce character varying not null,
title character varying not null,
age int not null )
```

### Create table on shard 1
```
CREATE TABLE movies (
id bigint not null,
category_id  int not null,
produce character varying not null,
title character varying not null,
age int not null,
CONSTRAINT category_id_check CHECK ( category_id = 1 )
);
```

### Create table on shard 2
```
CREATE TABLE movies (
id bigint not null,
category_id  int not null,
produce character varying not null,
title character varying not null,
age int not null,
CONSTRAINT category_id_check CHECK ( category_id = 2 )
);
```

### Create index on table shard field
```
CREATE INDEX movies_category_id_idx ON movies USING btree(category_id);
```

### Create foreign data wrapper
```
CREATE EXTENSION postgres_fdw;
CREATE SERVER shard_1 FOREIGN DATA WRAPPER postgres_fdw OPTIONS( host 'postgres_shard_slave1', port '5432', dbname 'postgres' );
CREATE SERVER shard_2 FOREIGN DATA WRAPPER postgres_fdw OPTIONS( host 'postgres_shard_slave2', port '5432', dbname 'postgres' );
CREATE USER MAPPING FOR postgres SERVER shard_1 OPTIONS (user 'postgres', password 'postgres');
CREATE USER MAPPING FOR postgres SERVER shard_2 OPTIONS (user 'postgres', password 'postgres');
```

### Create foreign tables on main
```
CREATE FOREIGN TABLE movies_shard_1 (
id bigint not null,
category_id  int not null,
produce character varying not null,
title character varying not null,
age int not null )
SERVER shard_1
OPTIONS (schema_name 'public', table_name 'movies');

CREATE FOREIGN TABLE movies_shard_2 (
id bigint not null,
category_id  int not null,
produce character varying not null,
title character varying not null,
age int not null )
SERVER shard_2
OPTIONS (schema_name 'public', table_name 'movies');
```

## Perfomance test
### Without sharding
Change port in file app.py to 5432 and run it:
```
python app.py 
```
Output:
```
254.81361532211304
253.71361532211304
252.48405337333679
253.43478932729852
254.01895332336426
```

### With sharding
Change port in file perfomance.py to 5433 and run it:
```
python app.py 
```
Output:
```
254.8136443211304
253.7645641211333
252.4840533733367
253.7526432423942
254.8740234829342
```