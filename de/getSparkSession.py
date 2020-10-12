import pyspark as ps    # for the pyspark suite

def getSparkSession():
        # we try to create a SparkSession to work locally on all cpus available
    spark = ps.sql.SparkSession.builder \
        .master("local[4]") \
        .appName("individual") \
        .getOrCreate()
    return spark