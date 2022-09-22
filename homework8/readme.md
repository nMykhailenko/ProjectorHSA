|   | without index  | BTREE index  | HASH index  |   
|---|---|---|---|
|select * from projector.users where birthdate='2017-02-14' | 2 s 477 ms  | 61 ms | 113 ms |   


INSERT 40 000 000 rows
|    | innodb_flush_log_at_trx_commit=0 | innodb_flush_log_at_trx_commit=1 |innodb_flush_log_at_trx_commit=2 |
|---|---|---|---|
|time   | 0:00:11.246109  | 0:00:07.875213  | 0:00:08.142193 |