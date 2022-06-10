import requests
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': '127.17.0.1', 'port': 9200}])

doc = requests.get('http://0.0.0.0/drinks/all').content
print(doc)
doc = doc.decode('utf-8')
doc = doc.replace("[","")
doc = doc.replace("]","")
doc = doc.replace("},","}/n")

test = doc.split("/n")
num =1
# for i in test:
#     resp = es.index(index="store", id=num, document=i)
#     num = num+1


# resp = es.get(index="store", id=100)
# print(resp['_source'])