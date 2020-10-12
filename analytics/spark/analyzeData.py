def analyzeUberData(sc):
    ut = sc.textFile("/home/mddarr/DalinarSoftware/Pipelines/data/uber.csv")
    rows = ut.map(lambda line: line.split(","))
    count = rows.map(lambda row: row[0]).distinct().count()
    print(count)
    hockeyTeams = sc.parallelize(("wild", "blackhawks", "red wings", "wild", "oilers", "whalers", "jets", "wild"))
    hockeyTeams.map(lambda k: (k, 1)).countByKey().items()

from Pipelines.getSparkSession import getSparkSession
import os

def process_song_data(spark, output_bucket):
    '''
    Read data into a dataframe and then write it to partitoned parquet files in the output_bucket
    :param spark:
    :param output_bucket:
    :return:
    '''
    song_data = os.getcwd() + '/data/song_data/*/*/*/*.json'
    songs_df = spark.read.json(song_data)
    songs_table = songs_df.select("song_id", "title", "artist_id", "year", "duration")

    output_path = os.path.join(output_bucket, "songs_table.parquet")
    print(output_path)
    if os.path.exists(output_path):
        songs_table.write.parquet(path=output_path,
                                  partitionBy=('year','artist_id'),
                                  mode="overwrite")
    else:
        songs_table.write.parquet(path=output_path,
                                  partitionBy=('year', 'artist_id'),
                                  mode="append")
    return songs_table

def process_log_data(spark, input_data_path, out_data_path):
    log_df = spark.read.json(input_data_path)
    songs_df.select(["artist_id", "artist_name", "artist_location", "artist_latitude", "artist_longitude"])
    return log_df

def create_artists_table(spark, df, out_data_path):
    artists_table = df.select(["artist_id", "artist_name", "artist_location", "artist_latitude", "artist_longitude"])
    output_path_artists = os.path.join(out_data_path, "artists_table")
    artists_table.write.parquet(path=output_path_artists, mode="append")

def create_users_table(spark, df, out_data_path):
    users_table = df.select(["userId", "firstName", "lastName", "artist_location", "gender", "level"])
    output_path_users = os.path.join(out_data_path, "artists_table")
    users_table.write.parquet(path=output_path_users, mode="append")

spark = getSparkSession()
output_bucket = "s3a://basedjango/parquet_files/"
songs_df = process_song_data(spark, output_bucket)
log_data_path = os.getcwd() + '/data/log_data/*.json'
log_df = process_log_data(spark,log_data_path, output_bucket )

