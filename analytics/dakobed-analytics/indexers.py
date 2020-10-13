from spark_session import getSparkInstance
import pandas as pd
spark = getSparkInstance()


pdf = pd.DataFrame({
        'x1': ['a','a','b','b', 'b', 'c'],
        'x2': ['apple', 'orange', 'orange','orange', 'peach', 'peach'],
        'x3': [1, 1, 2, 2, 2, 4],
        'x4': [2.4, 2.5, 3.5, 1.4, 2.1,1.5],
        'y1': [1, 0, 1, 0, 0, 1],
        'y2': ['yes', 'no', 'no', 'yes', 'yes', 'yes']
    })
df = spark.createDataFrame(pdf)
df.show()


from pyspark.ml.feature import StringIndexer

# build indexer
string_indexer = StringIndexer(inputCol='x1', outputCol='indexed_x1')
# learn the model
string_indexer_model = string_indexer.fit(df)
# transform the data
df_stringindexer = string_indexer_model.transform(df)
# resulting df
df_stringindexer.show()


df_ohe = df.select('x1')
df_ohe.show()

df_x1_indexed = StringIndexer(inputCol='x1', outputCol='indexed_x1').fit(df_ohe).transform(df_ohe)
df_x1_indexed.show()