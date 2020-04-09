import pandas as pd
import numpy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
from nltk import tokenize
import matplotlib.pyplot as plt

#read csv
df = pd.read_csv('news.csv')
#remove time from date
df['publish_date'] = df['publish_date'].apply(lambda x: x.split()[0])
df['publish_date'] = pd.to_datetime(df['publish_date'])
#filter only 2020 results
df = df[df['publish_date']>pd.to_datetime('2019')]

sid = SentimentIntensityAnalyzer()
data = pd.DataFrame(columns=['date', 'negative', 'positive'])

for row in df.itertuples():
  #analyze text and store into df
    text = row.text
    ss = sid.polarity_scores(text)
    data = data.append({
      'date':row.publish_date,
      'negative':ss['neg'],
      'positive':ss['pos']
      },ignore_index=True)

#plot result
data = data.groupby('date').mean()
data.plot(figsize=(20,10),title='CBC Dataset Sentiment Analysis')
