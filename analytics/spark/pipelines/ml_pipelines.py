import findspark
findspark.init()
import pyspark as ps
import os
import pyspark.sql.types as tp
from pyspark.sql.functions import array_contains


java8_location= '/usr/lib/jvm/java-8-openjdk-amd64' # Set your own
os.environ['JAVA_HOME'] = java8_location

spark = ps.sql.SparkSession.builder \
    .master("local[4]") \
    .appName("individual") \
    .getOrCreate()

my_schema = tp.StructType([
    tp.StructField(name= 'Batsman',      dataType= tp.IntegerType(),   nullable= True),
    tp.StructField(name= 'Batsman_Name', dataType= tp.StringType(),    nullable= True),
    tp.StructField(name= 'Bowler',       dataType= tp.IntegerType(),   nullable= True),
    tp.StructField(name= 'Bowler_Name',  dataType= tp.StringType(),    nullable= True),
    tp.StructField(name= 'Commentary',   dataType= tp.StringType(),    nullable= True),
    tp.StructField(name= 'Detail',       dataType= tp.StringType(),    nullable= True),
    tp.StructField(name= 'Dismissed',    dataType= tp.IntegerType(),   nullable= True),
    tp.StructField(name= 'Id',           dataType= tp.IntegerType(),   nullable= True),
    tp.StructField(name= 'Isball',       dataType= tp.BooleanType(),   nullable= True),
    tp.StructField(name= 'Isboundary',   dataType= tp.BinaryType(),   nullable= True),
    tp.StructField(name= 'Iswicket',     dataType= tp.BinaryType(),   nullable= True),
    tp.StructField(name= 'Over',         dataType= tp.DoubleType(),    nullable= True),
    tp.StructField(name= 'Runs',         dataType= tp.IntegerType(),   nullable= True),
    tp.StructField(name= 'Timestamp',    dataType= tp.TimestampType(), nullable= True)
])
data = spark.read.csv('data/ind-ban-comment.csv',schema= my_schema,header= True)
data = data.drop(*['Batsman', 'Bowler', 'Id'])
data.columns

import pyspark.sql.functions as f

# null values in each column
data_agg = data.agg(*[f.count(f.when(f.isnull(c), c)).alias(c) for c in data.columns])
data_agg.show()




from pyspark.ml.feature import StringIndexer, OneHotEncoderEstimator

# create object of StringIndexer class and specify input and output column
SI_batsman = StringIndexer(inputCol='Batsman_Name',outputCol='Batsman_Index')
SI_bowler = StringIndexer(inputCol='Bowler_Name',outputCol='Bowler_Index')

# transform the data
data = SI_batsman.fit(data).transform(data)
data = SI_bowler.fit(data).transform(data)

# view the transformed data
data.select('Batsman_Name', 'Batsman_Index', 'Bowler_Name', 'Bowler_Index').show(10)

