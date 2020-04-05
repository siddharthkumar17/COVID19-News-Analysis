import os
from dotenv import load_dotenv
from newsapi import NewsApiClient
import json
import requests

load_dotenv()
APIKEY = os.getenv('APIKEY')
newsapi = NewsApiClient(api_key=APIKEY)
query = 'virus OR pandemic OR disease OR infection OR covid OR covid19 OR coronavirus'
url = ('http://newsapi.org/v2/everything?q='+query+'&pageSize=100'+'&apiKey='+APIKEY)
data=[]
temp = requests.get(url).json()
for y in temp['articles']:
    data.append(y)
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
