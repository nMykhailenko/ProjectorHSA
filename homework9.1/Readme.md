# Redis master-slave cluster with 3 sentinels
 
## 1. Run docker container with Redis-Cluster and sentinel
 - `cd deployments` 
 - `docker-compose up` 
 
## 2. Run a few application in different terminals
```
python app.py 
python app.py -u 2
```

User with id = 1:
![image](https://user-images.githubusercontent.com/11583344/203132948-3ed43360-f2d9-48fb-a9ad-3b4954b360e8.png)

User with id = 2
![image](https://user-images.githubusercontent.com/11583344/203133050-3b683ca9-626e-4374-8f89-e4a322f0790b.png)
