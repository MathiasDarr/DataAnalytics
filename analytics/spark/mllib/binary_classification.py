from spark_session import getSparkInstance
from pyspark.ml.linalg import Vectors
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.regression import LinearRegression

# load packages
import sys
import pandas as pd
import matplotlib
import numpy as np
import scipy as sp

from pyspark.ml.classification import LinearSVC, LogisticRegression, DecisionTreeClassifier, GBTClassifier, RandomForestClassifier, \
    NaiveBayes, MultilayerPerceptronClassifier, OneVsRest

spark = getSparkInstance()

data_raw = spark.read.csv('data/titanic/train.csv', inferSchema=True, header=True)
data_val = spark.read.csv('data/titanic/test.csv', inferSchema=True, header=True)


# then we convert the boolean values to int (0 and 1), then we can count how many 1's exist in each column.
print('-'*25)
print('0: is not NULL')
print('1: is NULL')
print('-'*25)
print(' '*25)
# we build column strings and then use eval() to convert strings to column expressions.
data_raw.select([eval('data_raw.' + x + '.isNull().cast("int").alias("' + x + '")') for x in data_raw.columns]).show(n=10)


print('Train columns with null values:')
print('-'*25)
data_raw.select([eval('data_raw.' + x + '.isNull().cast("int").alias("' + x + '")') for x in data_raw.columns]).\
    groupBy().sum().toPandas()

print('Test columns with null values:')
print('-'*25)
data_val.select([eval('data_val.' + x + '.isNull().cast("int").alias("' + x + '")') for x in data_val.columns]).\
    groupBy().sum().toPandas()