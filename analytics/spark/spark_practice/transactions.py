from pyspark.sql.types import IntegerType, StringType, StructField,StructType, DateType, FloatType
from Pipelines.getSparkSession import getSparkSession
from pyspark.sql.functions import unix_timestamp, from_unixtime
from pyspark.sql.functions import array_contains
import os
spark = getSparkSession()
sc = spark.sparkContext


import json
#1. Load a dataframe users from data/users.txt instead using spark.read.csv with the following parameters: no headers,
# use separator ";", and infer the schema of the underlying data (for now). Use .show(5) and .printSchema() to check the result.
usersRDD = spark.read.csv(os.getcwd() + '/data/users.txt', sep=";")

data_schema = StructType([
               StructField('user_id', IntegerType(),True),
               StructField('name', StringType(),True),
               StructField('email', StringType(),True),
               StructField('phonenumber', StringType(), True)])

#3. Load an RDD transactions_rdd from data/transactions.txt instead using sc.textFile. Use .take(5) to check the result.
#Use .map() to split those csv-like lines, to strip the dollar sign on the second column, and to cast each column to its proper type.
#4. Create a schema for this dataset using proper names and types for the columns, using types from the pyspark.sql.types module (see lecture).
# #Use that schema to convert transactions_rdd into a dataframe transactions and use .show(5) and .printSchema() to check the result.


transactions_schema = StructType([
               StructField('user_id', IntegerType(),True),
               StructField('amount', FloatType(),True),
               StructField('date', StringType(),True)])
transactionsRDD = sc.textFile(os.getcwd() + '/data/transactions.txt')
transactionsRDD = transactionsRDD.map(lambda x: x.split(";"))
transactionsRDD = transactionsRDD.map(lambda row:(int(row[0]), float(row[1][1:]), row[2]))
transactionsDF = transactionsRDD.toDF(schema=transactions_schema)
#  for row in transactionsRDD.take(transactionsRDD.count()): print(row[1])     -> access the transaction amount..



#  Write a sequence of transformations or a SQL query that returns the names and the amount paid for the users with the top 10 transaction amounts.
# First let's experiment and return all the rows after a certain date? Seems pretty simple

# result = spark.sql("SELECT name, city, state, stars FROM yelp LIMIT 10")
from pyspark.sql.functions import to_date, udf
transactionsDF.createOrReplaceTempView('transactions')
transactionsDF = transactionsDF.select( to_date(transactionsDF.date, 'yyyy-MM-dd')).collect()
transactions2015 = spark.sql("SELECT * FROM transactions WHERE year(date) =2015")

usersDF = spark.read.csv(os.getcwd() + '/data/users.txt', sep=";", schema=data_schema)
usersDF.createOrReplaceTempView('users')


top10transactions = spark.sql("SELECT user_id, amount FROM transactions ORDER BY amount desc limit 10")
top10transactions.createOrReplaceTempView('top10transactions')
top10Users = spark.sql("SELECT name, amount FROM top10transactions INNER JOIN users on top10transactions.user_id = users.user_id ORDER BY amount desc")
#
# df = spark.createDataFrame([('1997-02-28',)], ['t'])
# df = df.select( to_date(df.t, 'yyyy-MM-dd').alias('dt')).collect()
