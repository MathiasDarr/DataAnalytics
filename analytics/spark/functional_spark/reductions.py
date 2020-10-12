import findspark
findspark.init()
import pyspark as ps
import os

def getSparkInstance():
    java8_location= '/usr/lib/jvm/java-8-openjdk-amd64' # Set your own
    os.environ['JAVA_HOME'] = java8_location

    spark = ps.sql.SparkSession.builder \
        .master("local[4]") \
        .appName("individual") \
        .getOrCreate()
    return spark

spark = getSparkInstance()
sc = spark.sparkContext
data = [1, 2, 3, 4, 5]
distData = sc.parallelize(data)

