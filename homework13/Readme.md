# Logging

## Run project
```
cd deployment
docker-compose up
```
 
## Connect to database 
```
docker-compose exec mysql bash
mysql -uroot -pMaster123!
CREATE DATABASE test;
USE test;
```

## Run slow query
```
select sleep(4);
```

## Check results
Connect to Elasticsearch directly and query data or Open Kiabana interface: localhost:5601