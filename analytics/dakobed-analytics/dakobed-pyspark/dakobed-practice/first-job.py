import pyspark as ps    # for the pyspark suite
import json             # for parsing json formatted data
import csv              # for the split_csvstring function from Part 3.2.2
try:                    # Python 3 compatibility
    from StringIO import StringIO
except ImportError:
    from io import StringIO
import os               # for accessing env variables for AWS credentials

# Part 2.1
def parse_json_first_key_pair(json_string):
    """Returns the first (key,value) pair from a json encoded dictionary.
    Parameters
    ----------
    json_string (str): a string encoding a json dictionary
    Returns
    -------
    [k,v]: the first key (k) and value (v) pair in the input json dict
    Example
    -------
    >>> parse_json_first_key_pair(u'{"Jane": "2"}')
    (u'Jane', 2)
    """
    pass


# Part 3.2.2
def split_csvstring(input_string):
    """Parse a csv-like line and break the values into a list.
    Parameters
    ----------
    input_string (str): a csv-like string to work on
    Returns
    -------
    list : the list of the values
    Example
    -------
    >>> split_csvstring(u'a,b,0.7,"Oct 7, 2016",42,')
    ['a', 'b', '0.7', 'Oct 7, 2016', '42', '']
    """

    # we create a StringIO handler
    fio = StringIO(input_string)
    # and feed that into the csv.reader library which is (probably) the best way to parse those strings
    reader = csv.reader(fio, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True)

    # obtains the first line of the reader (which should be the only line)
    row_values = next(reader)

    return row_values


# Part 3.2.4
def make_row_dict(row_values, col_names, keep_keys_set):
    """Extract specific columns from a row (string) and operates some specific transformations on the values.
    Parameters
    ----------
    row_values (list): a list of the values of a given row
    col_names (list): a list of all the columns in row_string ordered as in row_string
    keep_keys_dict (set): the set of the columns we keep (anything else is discarded)
    Returns
    -------
    dict : a dictionary containing the key,value pairs we chose to keep
    Example
    -------
    >>> make_row_dict(['2012', '4', 'AA', '12478', '12892', '-4.00', '0.00', '-21.00', '0.00', '0.00', ''],\
    ['YEAR', 'MONTH', 'UNIQUE_CARRIER', 'ORIGIN_AIRPORT_ID', 'DEST_AIRPORT_ID', 'DEP_DELAY', 'DEP_DELAY_NEW', 'ARR_DELAY', 'ARR_DELAY_NEW', 'CANCELLED', ''],\
    {'DEST_AIRPORT_ID', 'ORIGIN_AIRPORT_ID', 'DEP_DELAY', 'ARR_DELAY'}
    {'ARR_DELAY': -17.0, 'DEST_AIRPORT_ID': '12892', 'DEP_DELAY': -4.0, 'ORIGIN_AIRPORT_ID': '12478'}
    """
    pass


# Part 3.3.1
def transformation_pipeline(input_raw_rdd):
    """Processes the airline RDD to obtain answers to the 4 questions in assignment.
    Parameters
    ----------
    input_raw_rdd (spark RDD): the RDD obtained from 's3a://mortar-example-data/airline-data'
    Returns
    -------
    tuple : answers to questions Q1, Q2, Q3, Q4
    """
    pass
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
    # launching the full pipeline we have designed in Part 4
    [dataq1, dataq2, dataq3, dataq4] = transformation_pipeline(airline_rdd)

    print("Top 10 departing airports that have the lowest average delay:{}".format(dataq1))

    print("Top 10 departing airports that have the highest average delay:{}".format(dataq2))

    print("Top 10 arriving airports that have the lowest average delay:{}".format(dataq3))

    print("Top 10 arriving airports that have the highest average delay:{}".format(dataq4))

