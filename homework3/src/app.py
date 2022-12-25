import requests
import random
import time

version = '1'
tid = 'UA-252690406-2'
type = 'event'
event = 'currency'
action = 'exchange'

source = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'

endpoint = 'https://www.google-analytics.com/collect'
headers={'User-Agent': 'My User Agent 1.0'}

while True:
    try:
        r = requests.get(url = source)
        j = r.json()
        for i in range(len(j)):
            cid = int(j[i]['r030'])
            value = j[i]['rate']
            label = j[i]['cc'] + '-UAH'
            
            payload = {
                'v':version,
                'tid':tid,
                'cid':cid,
                't':type,
                'ec':event,
                'ea':action,
                'el':label,
                'ev':str(int(value*10000))
            }          

            print(payload)
            
            r = requests.post(url = endpoint, data = payload, headers=headers)
            print(r)
    except Exception as e:
        print(e)

    time.sleep(60)