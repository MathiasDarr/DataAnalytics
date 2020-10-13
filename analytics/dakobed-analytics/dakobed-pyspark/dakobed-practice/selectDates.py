from datetime import datetime
from pyspark.sql.functions import to_date, udf
from pyspark.sql.types import DateType
from pyspark.sql.functions import unix_timestamp, from_unixtime
from Pipelines.getSparkSession import getSparkSession
spark = getSparkSession()
sc = spark.sparkContext


df = spark.createDataFrame([('1997-02-28',)], ['t'])
df.select(to_date(df.t, 'yyyy-MM-dd').alias('dt')).collect()


from pyspark.sql.functions import from_unixtime

df = spark.createDataFrame([("11/25/1991",), ("11/24/1991",), ("11/30/1991",)], ['date_str'])

df2 = df.select('date_str', from_unixtime(unix_timestamp('date_str', 'MM/dd/yyy')).alias('date'))

df2

df2.show()