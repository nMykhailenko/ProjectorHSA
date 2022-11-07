import json
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-w", "--word", help = "Word to search.  Current: value = 'bake'.")
parser.add_argument("-f", "--fuzziness", help = "Fuzziness. Choose: 0, 1, 2 or auto:low,high. Current: value = 'auto:1,3'.")
parser.add_argument("-fml", "--fuzzy_min_length", help = "Fuzzy min length. Current: value = 3.")
parser.add_argument("-fpl", "--fuzzy_prefix_length", help = "Prefix length.  Current: value = 1.")

args = parser.parse_args()
word = args.word if args.word else 'bake'
fuzziness = args.fuzziness if args.fuzziness else 'auto:1,3'
fuzzy_min_length = args.fuzzy_min_length if args.fuzzy_min_length else 3
fuzzy_prefix_length = args.fuzzy_prefix_length if args.fuzzy_prefix_length else 1

index = 'prjctr'
headers = {'content-type': 'application/json'}

data = json.dumps(
    {
        "suggest": {
            "word_suggest": {
                "prefix": word,
                "completion": {
                    "field": "word",
                    "size": 5,
                    "skip_duplicates": "true",
                    "fuzzy": {
                        "fuzziness": fuzziness,
                        "transpositions": "true",
                        "min_length": fuzzy_min_length,
                        "prefix_length": fuzzy_prefix_length
                    }
                }
            }
        }
    }
)

response = requests.get(f'http://localhost:9200/{index}/_search', headers=headers, data=data)
if response.status_code == 200:
    options = response.json()['suggest']['word_suggest'][0]['options']
    if len(options) > 0:
        for i in range(len(options)):
            print(options[i]['text'])