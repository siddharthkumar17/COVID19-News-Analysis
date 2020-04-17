
import findspark
findspark.init('C:/spark')


from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
import json
from pyspark.sql.types import *
from pyspark.sql.functions import *
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
import pandas as pd

spark = SparkSession.builder.master("local").appName("News Analysis").getOrCreate()
sc = spark.sparkContext
df = spark.read.json("data.json")


sid = SentimentIntensityAnalyzer()

schema = StructType([StructField("date", DateType(), True),StructField("negative", DecimalType(), True),StructField("positive", DecimalType(), True)])
data = spark.createDataFrame(sc.emptyRDD(), schema)

for row in df.toLocalIterator():
    text = row.description
    ss = sid.polarity_scores(text)
    newrow = spark.createDataFrame([{
      'date':row.publishedAt.split('T')[0],
      'negative':ss['neg'],
      'positive':ss['pos']
      }])
    data = data.union(newrow)

data.show()
pdf = data.toPandas().groupby('date').mean()
pdf.plot(figsize=(20,10),title='NewsAPI Dataset Sentiment Analysis')
