import requests
from elasticsearch import Elasticsearch
import json

es = Elasticsearch([{'host': '127.17.0.1', 'port': 9200}])

request_api = requests.get('http://0.0.0.0/drinks/all').content
request_api = request_api.decode('utf-8')

json_object = json.loads(request_api)
id =1

for i in json_object:
    print(i)
    resp = es.index(index="store", id=id, document=i)
    id = id+1