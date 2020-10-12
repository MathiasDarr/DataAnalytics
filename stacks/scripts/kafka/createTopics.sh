#! /bin/bash
${CONFLUENT_HOME}/bin/kafka-topics --create --topic $1 \
 --zookeeper localhost:2181 --partitions 1 --replication-factor 1