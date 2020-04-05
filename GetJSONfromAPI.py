import os
from dotenv import load_dotenv
from newsapi import NewsApiClient
import json

load_dotenv()
APIKEY = os.getenv('APIKEY')
newsapi = NewsApiClient(api_key=APIKEY)
query = 'virus OR pandemic OR disease OR infection OR covid OR covid19 OR coronavirus'
data = []
for x in range(1,5):
    temp = newsapi.get_everything(q=query,language='en',sort_by='relevancy',page=x)
    for y in temp['articles']:
        data.append(y)
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
