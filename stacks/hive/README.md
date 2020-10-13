[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/big-data-europe/Lobby)

# docker-hive

This is a docker container for Apache Hive 2.3.2. It is based on https://github.com/big-data-europe/docker-hadoop so check there for Hadoop configurations.
This deploys Hive and starts a hiveserver2 on port 10000.
Metastore is running with a connection to postgresql database.
The hive configuration is performed with HIVE_SITE_CONF_ variables (see hadoop-hive.env for an example).

docker-compose exec hive-server bash


## Create a table
CREATE TABLE pokes (foo INT, bar STRING);

## List tables
show tables


## launch presto server

wget https://repo1.maven.org/maven2/io/prestosql/presto-cli/308/presto-cli-308-executable.jar
mv presto-cli-308-executable.jar presto.jar
chmod +x presto.jar


Hive vs Presto

Hive translates SQL queries into multiple stages of MapReduce and it is powerful enough to handle huge numbers of jobs. MapReduce is fault-tolerant since it stores the intermediate results into disks and enables batch-style data processing.
 A key advantage of Hive over newer SQL-on-Hadoop engines is robustness: Other engines like Cloudera’s Impala and Presto require careful optimizations when two large tables (100M rows and above) are joined. Hive can join tables with billions of rows with ease and should the jobs fail it retries automatically. Furthermore, Hive itself is becoming faster as a result of the Hortonworks Stinger initiative.

Hive is optimized for query throughput, while Presto is optimized for latency. Presto has a limitation on the maximum amount of memory that each task in a query can store, so if a query requires a large amount of memory, the query simply fails. Such error handling logic (or a lack thereof) is acceptable for interactive queries; however, for daily/weekly reports that must run reliably, it is ill-suited. For such tasks, Hive is a better alternative.

In terms of data-processing models, Hive is often described as a pull model, since its MapReduce stage pulls data from the preceding tasks. Presto follows the push model, which is a traditional implementation of DBMS, processing a SQL query using multiple stages running concurrently. An upstream stage receives data from its downstream stages, so the intermediate data can be passed directly without using disks. If the query consists of multiple stages, Presto can be 100 or more times faster than Hive.






