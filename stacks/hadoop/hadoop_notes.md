### Running Hadoop in Docker

http://localhost:9870/

docker exec -it namenode bash


## Create some input text files
$ mkdir input
$ echo "Hello World" >input/f1.txt
$ echo "Hello Docker" >input/f2.txt

## Create input directory on HDFS
hadoop fs -mkdir -p input

## Place input files on HDFS
hdfs dfs -put ./input/* input

## List all files in hdfs
hadoop fs -ls