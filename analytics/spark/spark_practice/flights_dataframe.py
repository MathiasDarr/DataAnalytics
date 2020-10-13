import findspark
findspark.init()
import pyspark as ps
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import os
import json

def getSparkInstance():
    """
    @return: Return Spark session
    """
    java8_location= '/usr/lib/jvm/java-8-openjdk-amd64' # Set your own
    os.environ['JAVA_HOME'] = java8_location
    spark = ps.sql.SparkSession.builder \
        .master("local[4]") \
        .appName("individual") \
        .getOrCreate()
    return spark

spark = getSparkInstance()

# Read and create a temporary view
# Infer schema (note that for larger files you
# may want to specify the schema)

spark.sql("CREATE DATABASE dakobed_spark_db")
spark.sql("USE dakobed_spark_db")


## Create a managed table using spark sql
spark.sql("CREATE TABLE managed_us_delay_flights_tbl (date STRING, delay INT, distance INT, origin STRING, destination STRING)")

## Or you can accomplish the same thing using the dataframe API


csv_file = "data/departuredelays.csv"
# Schema as defined in the preceding example
schema="date STRING, delay INT, distance INT, origin STRING, destination STRING"
flights_df = spark.read.csv(csv_file, schema=schema)
flights_df.write.saveAsTable("managed_us_delay_flights_tbl")


### Or you can create an unmanaged table by doing ..

spark.sql("""CREATE TABLE us_delay_flights_tbl(date STRING, delay INT,
distance INT, origin STRING, destination STRING)
USING csv OPTIONS (PATH'data/departuredelays.csv')""")

# Or create the unmanaged table using the dataframe API like..

flights_df.write \
    .option("path", "/tmp/data/us_flights_delay") \
    .saveAsTable("us_delay_flights_tbl")


df = spark.read.format("csv") \
    .option("inferSchema", "true") \
    .option("header", "true") \
    .load(csv_file)

df.createOrReplaceTempView("us_delay_flights_tbl")

spark.sql("""SELECT distance, origin, destination
FROM us_delay_flights_tbl WHERE distance > 1000
ORDER BY distance DESC""").show(10)


spark.sql("""
    SELECT delay, origin, destination,
    CASE
        WHEN delay > 360 THEN 'Very Long Delays'
        WHEN delay > 120 AND delay < 360 THEN 'Long Delays'
        WHEN delay > 60 AND delay < 120 THEN 'Short Delays'
        WHEN delay > 0 and delay < 60 THEN 'Tolerable Delays'
        WHEN delay = 0 THEN 'No Delays'
        ELSE 'Early'
    END AS Flight_Delays
    FROM us_delay_flights_tbl
    ORDER BY origin, delay DESC""").show(10)

## This statement can be written equivalently as

df.select("distance", "origin", "destination") \
    .where("distance")
