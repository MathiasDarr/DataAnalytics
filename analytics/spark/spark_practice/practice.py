from Pipelines.getSparkSession import getSparkSession
import json

def parse_json_first_key_pair(json_string):
    js = json.loads(json_string)
    key = list(js.keys())[0]
    value = int(list(js.values())[0])
    return (key, value)

spark = getSparkSession()
sc = spark.sparkContext
file_rdd = sc.textFile('data/cookie_data.txt')
parsedRDD = file_rdd.map(lambda x: parse_json_first_key_pair(x))
filteredRDD =  parsedRDD.filter(lambda x: x[1]>5)

#For each name return the entry with the max number of cookies
maxRDD =parsedRDD.reduceByKey(max)

# Show the first results using .sortBy() and take(). sortBy() requrires a lmbda that ouptuts the the value/quantity on which we
# want to sort our rows

sortByMaxRDD = maxRDD.sortBy(lambda x:x[1])

# To get the maximum profit we can either use a map and a sum or reduce after calling .values()
maxprofit = sortByMaxRDD.map(lambda x:x[1]).sum()
profit = sortByMaxRDD.values().reduce(lambda x,y:x+y)
