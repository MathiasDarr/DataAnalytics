import findspark
findspark.init()
import pyspark as ps
from pyspark.sql.functions import array_contains

import os

java8_location= '/usr/lib/jvm/java-8-openjdk-amd64' # Set your own
os.environ['JAVA_HOME'] = java8_location

spark = ps.sql.SparkSession.builder \
    .master("local[4]") \
    .appName("individual") \
    .getOrCreate()

sc = spark.sparkContext

yelpDF = spark.read.json(os.getcwd() + '/data/yelp.json')
# Call the createOrReplaceTempView method so thaqt we can query this dataframe with the spark.sql
yelpDF.createOrReplaceTempView('yelp')
# result = spark.sql("SELECT name, city, state, stars FROM yelp LIMIT 10")

# 3. Write a query or a sequence of transformations that returns the name of entries that fulfill the following conditions:
#    Rated at 5 stars
#    In the city of Phoenix
#    Accepts credit card (Reference the 'Accepts Credit Card' field by attributes.`Accepts Credit Cards`. NOTE: We are actually looking for the value 'true', not the boolean value True!)
#    Contains Restaurants in the categories array.

FiveStarsPheonixCC = spark.sql("SELECT name, city,categories, stars FROM yelp WHERE city='Phoenix' and stars=5")
from pyspark.sql import functions as F
containsRestaurants = FiveStarsPheonixCC.filter(array_contains(F.col("categories"), "Food"))


#
# categories = yelpDF.select(yelpDF[2])
# d = categories.select()
# categories.select()
#
#
# categories.createOrReplaceTempView('categories')
# # c =  spark.sql("SELECT * FROM categories LATERAL VIEW explode(categories) c AS cats;")
# categories.filter()