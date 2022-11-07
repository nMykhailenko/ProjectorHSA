# Elasticsearch autocomplete 
 
## 1. Run docker container with Elasticsearch 
`docker-compose up` 
 
## 2. Create index and seed with data 
`python initialize_elastic.py` 
 
## 3. See search help 
`python search.py --help`

 
## 4. Request autocomplete for prefix 
 `python search.py -w 'bake'` 
 
Output 
```
ba
baa
baba
babas
babble
``` 
 