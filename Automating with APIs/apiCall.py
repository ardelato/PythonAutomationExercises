import requests
import json

baseUrl = 'https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc' : '012993441012'}
response = requests.get(baseUrl,params=parameters)

content = response.content

info = json.loads(content)
print(type(info))
print(info)

items = info.get('items')
itemInfo = items[0]
title = itemInfo.get('title')
brand = itemInfo.get('brand')
print(title)
print(brand)