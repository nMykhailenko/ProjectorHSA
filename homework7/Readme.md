# Cache images using Nginx WebServer for Fine Tuning 
 
## Run 
Run docker container from main project folder 
`cd deployment`
`docker-compose up`

## Use it 
### 1. Request image first time: 
`curl -D - localhost/images/test.png --output temp.png` 
 
We get *X-Cache-Status: MISS* and file size *65484*:
```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0HTTP/1.1 200 OK
Server: nginx/1.23.2
Date: Sun, 18 Dec 2022 21:12:27 GMT
Content-Type: text/plain
Content-Length: 8513
Connection: keep-alive
Last-Modified: Sun, 18 Dec 2022 21:07:33 GMT
ETag: "639f8115-2141"
X-Cache-Status: MISS
Accept-Ranges: bytes

100  8513  100  8513    0     0  64566      0 --:--:-- --:--:-- --:--:-- 65484
```
 
### 2. Request image second time: 
`curl -D - localhost/images/test.png --output temp.png` 
 
In output we get *X-Cache-Status: MISS* and file size *65484*:
```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0HTTP/1.1 200 OK
Server: nginx/1.23.2
Date: Sun, 18 Dec 2022 21:12:27 GMT
Content-Type: text/plain
Content-Length: 8513
Connection: keep-alive
Last-Modified: Sun, 18 Dec 2022 21:07:33 GMT
ETag: "639f8115-2141"
X-Cache-Status: MISS
Accept-Ranges: bytes

100  8513  100  8513    0     0  64566      0 --:--:-- --:--:-- --:--:-- 65484
```
 
### 3. Request image third time and get it from cache: 
`curl -D - localhost/images/test.png --output temp.png` 

In output we get *X-Cache-Status: HIT* and file size *65992*:
``` 
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0HTTP/1.1 200 OK
Server: nginx/1.23.2
Date: Sun, 18 Dec 2022 21:13:16 GMT
Content-Type: text/plain
Content-Length: 8513
Connection: keep-alive
Last-Modified: Sun, 18 Dec 2022 21:07:33 GMT
ETag: "639f8115-2141"
X-Cache-Status: HIT
Accept-Ranges: bytes

100  8513  100  8513    0     0  65150      0 --:--:-- --:--:-- --:--:-- 65992
```

### 4. Replace image with other
```
mv data/images/test.png data/images/test1.png 
``` 

### 5. Request image fourth time and get old one from cache: 
`curl -D - localhost/images/test.png --output temp.png` 

In output we get *X-Cache-Status: HIT* and file size *65992*:
``` 
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0HTTP/1.1 200 OK
Server: nginx/1.23.2
Date: Sun, 18 Dec 2022 21:16:08 GMT
Content-Type: text/plain
Content-Length: 8513
Connection: keep-alive
Last-Modified: Sun, 18 Dec 2022 21:07:33 GMT
ETag: "639f8115-2141"
X-Cache-Status: HIT
Accept-Ranges: bytes

100  8513  100  8513    0     0  65150      0 --:--:-- --:--:-- --:--:-- 65992
``` 
