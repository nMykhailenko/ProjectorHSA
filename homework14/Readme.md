# DDos Block 

## Run
Run every time for rebuild and restart containers
```
docker-compose down
docker-compose build
docker-compose up
```

## UDP Flood 
`
hping3 --udp -i u100  localhost -p 80
`

Result:
```
ddos_block-ddos-1   | ICMP Port Unreachable from ip=127.0.0.1 name=localhost 
ddos_block-ddos-1   | status=0 port=12613 seq=11062
ddos_block-ddos-1   | ICMP Port Unreachable from ip=127.0.0.1 name=localhost
ddos_block-ddos-1   | status=0 port=12614 seq=11063
ddos_block-ddos-1   | ICMP Port Unreachable from ip=127.0.0.1 name=localhost
ddos_block-ddos-1   | status=0 port=12615 seq=11064
```


## ICMP flood 
`
hping3 -1 -i u100  localhost -p 80
`

Result:
```
ddos_block-ddos-1   | len=28 ip=127.0.0.1 ttl=64 id=48842 icmp_seq=1973 rtt=12.5 ms
ddos_block-ddos-1   | len=28 ip=127.0.0.1 ttl=64 id=48843 icmp_seq=1974 rtt=12.4 ms
ddos_block-ddos-1   | len=28 ip=127.0.0.1 ttl=64 id=48844 icmp_seq=1975 rtt=12.2 ms
ddos_block-ddos-1   | len=28 ip=127.0.0.1 ttl=64 id=48845 icmp_seq=1976 rtt=12.1 ms
ddos_block-ddos-1   | len=28 ip=127.0.0.1 ttl=64 id=48846 icmp_seq=1977 rtt=11.7 ms
ddos_block-ddos-1   | len=28 ip=127.0.0.1 ttl=64 id=48847 icmp_seq=1978 rtt=11.3 ms
ddos_block-ddos-1   | len=28 ip=127.0.0.1 ttl=64 id=48848 icmp_seq=1979 rtt=11.3 ms
--- localhost hping statistic ---
53554 packets transmitted, 53454 packets received, 1% packet loss
round-trip min/avg/max = 1.6/18.9/1017.3 ms
```


## HTTP flood 
`
hping3 -i u100  localhost
`

Result:
```
ddos_block-ddos-1   | len=40 ip=127.0.0.1 ttl=64 DF id=0 sport=0 flags=RA seq=11940 win=0 rtt=11.4 ms      
ddos_block-ddos-1   | len=40 ip=127.0.0.1 ttl=64 DF id=0 sport=0 flags=RA seq=11941 win=0 rtt=11.3 ms      
ddos_block-ddos-1   | len=40 ip=127.0.0.1 ttl=64 DF id=0 sport=0 flags=RA seq=11942 win=0 rtt=11.2 ms      
ddos_block-ddos-1   | len=40 ip=127.0.0.1 ttl=64 DF id=0 sport=0 flags=RA seq=11943 win=0 rtt=11.0 ms      
ddos_block-ddos-1   | len=40 ip=127.0.0.1 ttl=64 DF id=0 sport=0 flags=RA seq=11944 win=0 rtt=10.9 ms      
ddos_block-ddos-1   | len=40 ip=127.0.0.1 ttl=64 DF id=0 sport=0 flags=RA seq=11945 win=0 rtt=10.8 ms 
--- localhost hping statistic ---
88464 packets transmitted, 88401 packets received, 1% packet loss
round-trip min/avg/max = 1.2/18.7/1030.9 ms
```



## Slowloris 
```
pip install Slowloris
slowloris localhost -s 250 -fr
```

Result:
```
ddos_block-nginx-1      | 2022/12/18 13:13:43 [warn] 33#33: 50 worker_connections are not enough, reusing connections
ddos_block-nginx-1      | 192.168.56.1 - - [12/Dec/2022:13:13:43 +0000] "GET /?517 HTTP/1.1" 400 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50" "-"
ddos_block-nginx-1      | 192.168.56.1 - - [12/Dec/2022:13:13:43 +0000] "GET /?995 HTTP/1.1" 400 0 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36" "-"
ddos_block-nginx-1      | 192.168.56.1 - - [12/Dec/2022:13:13:43 +0000] "GET /?1896 HTTP/1.1" 400 0 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36" "-"
ddos_block-nginx-1      | 192.168.56.1 - - [12/Dec/2022:13:13:43 +0000] "GET /?904 HTTP/1.1" 400 0 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36" "-"
```

## SYN flood 
`
hping3 -S -q -n -i u100  localhost -p 80
`

Result:
```
HPING localhost (eth0 192.168.56.4): S set, 40 headers + 0 data bytes
--- localhost hping statistic ---
728994 packets transmitted, 728954 packets received, 1% packet loss
round-trip min/avg/max = 0.6/10.4/1014.0 ms
```

## Ping of Death 
`
ping -l 65509 localhost
`
