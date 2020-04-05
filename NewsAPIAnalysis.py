from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
import json
spark = SparkSession.builder.master("local").appName("News Analysis").getOrCreate()
sc = spark.sparkContext
df = spark.read.json("data.json",multiLine=True)