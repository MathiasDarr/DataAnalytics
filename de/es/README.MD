sysctl -w vm.max_map_count=262144

Move data from kafka into ES
# Create the topic 
docker exec -it broker kafka-topics --zookeeper zookeeper:2181 --create --topic elasticsearch --partitions 1 --replication-factor 1

# Produce to the topic
kafkacat -P -b localhost:9092 -t elasticsearch


# Query Elastic search

curl localhost:9200/elasticsearch/_search | jq


curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d '{
 "name": "simple-elasticsearch-connector"'
 "config": {
   "connector.class": "io.confluent.connect.elasticsearch.ElasticsearchSinkConnector",
   "connection.url": "http://elasticsearch:9200",
   "tasks.max": "1",
   "topics": "simple.elasticsearch.data"
   "type.name": "_doc"
 }
}'


