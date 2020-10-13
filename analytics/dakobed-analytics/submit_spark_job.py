import findspark
findspark.init()
import pyspark as ps
import os

java8_location= '/usr/lib/jvm/java-8-openjdk-amd64' # Set your own
os.environ['JAVA_HOME'] = java8_location

spark = ps.sql.SparkSession.builder \
    .master("local[4]") \
    .appName("individual") \
    .getOrCreate()

sc = spark.sparkContext

link = 'data/yelp.json'
yelp_rdd = sc.textFile(link)
print("There are dfdf " + str(yelp_rdd.count()))
