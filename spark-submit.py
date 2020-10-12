import pyspark as ps    # for the pyspark suite
from Pipelines.getSparkSession import getSparkSession
if __name__ == "__main__":
    # we try to create a SparkSession to work locally on all cpus available
    spark = ps.sql.SparkSession.builder \
            .master("local[4]") \
            .appName("individual") \
            .getOrCreate()

    # Grab sparkContext from the SparkSession object
    sc = spark.sparkContext
    sc.setLogLevel('ERROR')

    # link to the s3 repository from Part 3
    link = 's3a://mortar-example-data/airline-data'
    airline_rdd = sc.textFile(link)
    print("There are dfdf " + str(airline_rdd.count()))

<script src="https://gist.github.com/MathiasDarr/8696db293003278864127f40b1453b14.js"></script>

<script src="https://gist.github.com/MathiasDarr/88d316280e3c455f903c85d67a1d41e1.js"></script>