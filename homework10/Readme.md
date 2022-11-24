# Redis RDB, Redis AOF and Beanstalkd queue perfomance test

# Run containers
 - `cd deployment`
 - `docker-compose up`

# Build stress-tests
 - `cd ../tests/stress-tests`
 - `docker build -t projector-redis-queue .`

# URLs (Put 2 messages to queue and get 1 message)
redis-rdb.txt  
redis-aof.txt  
beanstalkd-urls.txt  

# Siege commands
```
docker run --rm --net redis-queue_projector-queue -t projector-redis-queue -c10 -t60s -f /app/{FILENAME_ABOVE} 
docker run --rm --net redis-queue_projector-queue -t projector-redis-queue -c25 -t60s -f /app/{FILENAME_ABOVE}
docker run --rm --net redis-queue_projector-queue -t projector-redis-queue -c50 -t60s -f /app/{FILENAME_ABOVE}
docker run --rm --net redis-queue_projector-queue -t projector-redis-queue -c100 -t60s -f /app/{FILENAME_ABOVE}
```

# Results
## Response time, secs
concurrent | Redis RDB | Redis AOF | Beanstalkd |  
--- | --- | --- | --- |  
10 | 0.04 | 0.06 | 0.07 |  
25 | 0.13 | 0.13 | 0.15 |  
50 | 0.21 | 0.24 | 0.27 |  
100 | 0.47 | 0.46 | 0.58 | 
 
## Transaction rate, trans/sec
concurrent | Redis RDB | Redis AOF | Beanstalkd |  
--- | --- | --- | --- |  
10 | 201.21 | 227.23 | 169.97 |  
25 | 215.21 | 201.34 | 173.85 |  
50 | 219.59 | 217.79 | 180.89 |  
100 | 220.21 | 224.69 | 181.53 |
 
## Longest transaction
concurrent | Redis RDB | Redis AOF | Beanstalkd |  
--- | --- | --- | --- |  
10 | 0.16 | 0.14 | 0.12 |  
25 | 0.27 | 0.26 | 0.30 |  
50 | 0.41 | 0.39 | 0.45 |  
100 | 0.60 | 0.58 | 0.77 |
