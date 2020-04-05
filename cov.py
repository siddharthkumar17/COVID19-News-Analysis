import pandas as pd
import numpy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
from nltk import tokenize
import matplotlib.pyplot as plt

df = pd.read_csv('news.csv')
df['publish_date'] = df['publish_date'].apply(lambda x: x.split()[0])
df['publish_date'] = pd.to_datetime(df['publish_date'])
df = df[df['publish_date']>pd.to_datetime('2019')]

sid = SentimentIntensityAnalyzer()

data = pd.DataFrame(columns=['date', 'negative', 'positive'])
for row in df.itertuples():
   
    text = row.text
    ss = sid.polarity_scores(text)
    
    data = data.append({
      'date':row.publish_date,
      'negative':ss['neg'],
      'positive':ss['pos']
      },ignore_index=True)
data = data.groupby('date').mean()
print(data)
data.plot(figsize=(20,10))
