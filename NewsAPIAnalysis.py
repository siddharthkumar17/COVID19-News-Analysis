from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
import json
from pyspark.sql.types import *
from pyspark.sql.functions import *
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
import pandas as pd

spark = SparkSession.builder.master("local").appName("News Analysis").getOrCreate()
sc = spark.sparkContext
df = spark.read.json("/FileStore/tables/data.json")


sid = SentimentIntensityAnalyzer()

schema = StructType([StructField("date", DateType(), True),StructField("negative", DecimalType(), True),StructField("positive", DecimalType(), True)])
data = sqlContext.createDataFrame(sc.emptyRDD(), schema)

for row in df.toLocalIterator():
    text = row.description
    ss = sid.polarity_scores(text)
    newrow = spark.createDataFrame([{
      'date':row.publishedAt.split('T')[0],
      'negative':ss['neg'],
      'positive':ss['pos']
      }])
    data = data.union(newrow)

pdf = data.toPandas().groupby('date').mean()
pdf.plot(figsize=(20,10),title='NewsAPI Dataset Sentiment Analysis')
