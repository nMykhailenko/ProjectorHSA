from email.mime import base
from urllib import response
import requests
import json

base_url = 'http://localhost:9200'
index_name = 'prjctr'
headers = {'content-type': 'application/json'}

print("Start Elastic health check")
response = requests.get(f'{base_url}/_cluster/health?wait_for_status=yellow&timeout=10s&pretty')
if response.status_code == 200:
    if response.json()['status'] in ('green', 'yellow'):
        print(f"Healthy with status: {response.json()['status']}")
    else:
        raise Exception(f"Unhealthy with status: {response.json()['status']}")
else:
    raise Exception("Error")
print("End Elastic health check \n")

print(f"Start checking that index: {index_name} exists")
response = requests.get(f'{base_url}/_aliases?pretty=true')
if response.status_code == 200:
    index_exists = index_name in response.json()
    if index_exists:
        print(f"Index '{index_name}' exists\n")
    else:
        print(f"Index '{index_name}' not found\n")
else:
    raise Exception("Error getting indexes information")


if index_exists == False:  
    print(f"Creating index '{index_name}'")

    data = json.dumps(
        {
            "mappings": {
                "properties": {
                    "word": {
                        "type": "search_as_you_type"
                        }
                    }       
                }
        }
    )

    response = requests.put(f'{base_url}/{index_name}', headers=headers, data=data)
    if response.status_code == 200:
        print(f"Index '{index_name}' created")
    else:
        raise Exception(f"Error cant create index '{index_name}' Ex: {response.json()} ")
    print(f"End creating index '{index_name}'\n")


print(f"Start checking '{index_name}' size")
response = requests.get(f'{base_url}/{index_name}/_stats')
if response.status_code == 200:
    index_size = response.json()['indices'][f'{index_name}']['total']['docs']['count']
    print(f"Index '{index_name}' size is {index_size} docs")
else:
    raise Exception(f"Request cannot get index '{index_name}' stats")
print(f"Finish checking '{index_name}' index size\n")

if index_size == 0:
    print(f"Start adding docs to '{index_name}' index")
    with open('engmix.txt') as f:
        words = f.readlines()
        dictionary_size = len(words)

    print(f"Read dictionary with size {dictionary_size} words")
    for i in range(dictionary_size):
        data = json.dumps(
            {
                "word":words[i]
            }
        )

        response = requests.put(f'{base_url}/{index_name}/_doc/{i+1}', headers=headers, data=data)
        if response.status_code != 201:
            raise Exception(f"Cannot put word '{words[i]}' with position {i} to '{index_name}' index")

    print(f"Finish adding docs to '{index_name}' index")

print("Elastic is ready")
