import pandas as pd
import numpy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
from nltk import tokenize

df = pd.read_csv('news.csv')
df['publish_date'] = pd.to_datetime(df['publish_date'])
# print(df['publish_date'])
# print(df.info())
df=df.sort_values(by=['publish_date'])
df=df.drop(df.index[:3])

print(df['publish_date'])
sid = SentimentIntensityAnalyzer()
for row in df.itertuples():
    #print(row)
    text = row.text
    print(text)
    ss = sid.polarity_scores(text)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]) )
    print()
    texttokens = tokenize.sent_tokenize(text)
    for token in texttokens:
        print(token)
        ss = sid.polarity_scores(token)
        for k in sorted(ss):
            print('{0}: {1}, '.format(k, ss[k]))


    break


