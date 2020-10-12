from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

def getSparkContext():
    conf = SparkConf().setAppName("app")
    sc = SparkContext(conf=conf)
    return sc

def create_spark_session():
    spark = SparkSession \
        .builder \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0") \
        .getOrCreate()
    return spark
