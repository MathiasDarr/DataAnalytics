from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler
from pyspark.ml import Pipeline

from spark_session import getSparkInstance
import pandas as pd
spark = getSparkInstance()

from pyspark.ml.feature import VectorAssembler


all_stages = [StringIndexer(inputCol=c, outputCol='idx_' + c) for c in ['x1', 'x2', 'x3']] + \
             [OneHotEncoder(inputCol='idx_' + c, outputCol='ohe_' + c) for c in ['x1', 'x2', 'x3']]



pdf = pd.DataFrame({
        'x1': ['a','a','b','b', 'b', 'c'],
        'x2': ['apple', 'orange', 'orange','orange', 'peach', 'peach'],
        'x3': [1, 1, 2, 2, 2, 4],
        'x4': [2.4, 2.5, 3.5, 1.4, 2.1,1.5],
        'y1': [1, 0, 1, 0, 0, 1],
        'y2': ['yes', 'no', 'no', 'yes', 'yes', 'yes']
    })
df = spark.createDataFrame(pdf)


df_new = Pipeline(stages=all_stages).fit(df).transform(df)
df_new.show()

df_assembled = VectorAssembler(inputCols=['ohe_x1', 'ohe_x2', 'ohe_x3', 'x4'], outputCol='featuresCol')\
    .transform(df_new)\
    .drop('idx_x1', 'idx_x2', 'idx_x3')

df_assembled.show(truncate=False)