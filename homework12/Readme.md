# Load-Balancing and delivery by GeoIP in Nginx

## Run project
```
cd deployment
docker-compose up
```
 
## Test
Call application
```
curl localhost
```
 
And see results.
For default:
```
<!DOCTYPE html>
<html>
<body>
<h1>The Other Countries</h1>
</body>
```
```
load-balancing-app_other-1        | 69.162.81.2 - - [27/Nov/2022:20:40:16 +0000] "GET / HTTP/1.0" 200 79 "-" "curl/7.83.1" "-"
load-balancing-load-balancer-1    | 69.162.81.1 - - [27/Nov/2022:20:40:16 +0000] "GET / HTTP/1.1" 200 79 "-" "curl/7.83.1" "-"
```

 
For The USA:
```
<!DOCTYPE html>
<html>
<body>
<h1>The United States</h1>
</body>
```
