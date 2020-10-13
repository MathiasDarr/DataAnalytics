from analyzeData import analyzeUberData
import pyspark as ps


if __name__ == '__main__':

    spark  = SparkSession \
        .builder \
        .enableHiveSupport() \
        .config(conf=SparkConf().set("spark.driver.maxResultSize", "2g")) \
        .appName("test") \
        .getOrCreate()
    analyzeUberData(spark)
