import os
import findspark
findspark.init()
import pyspark as ps

java8_location= '/usr/lib/jvm/java-8-openjdk-amd64' # Set your own
os.environ['JAVA_HOME'] = java8_location

spark = ps.sql.SparkSession.builder \
    .master("local[4]") \
    .appName("individual") \
    .getOrCreate()

sc = spark.sparkContext

ut = sc.textFile("data/uber.csv")
rows = ut.map(lambda line: line.split(","))
count = rows.map(lambda row: row[0]).distinct().count()
print(count)


