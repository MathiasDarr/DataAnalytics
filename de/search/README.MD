Reproduction steps
# Install the Debezium connector
docker exec connect confluent-hub install debezium/debezium-connector-postgresql:0.9.4
confluent-hub install debezium/debezium-connector-postgresql:0.9.4

# List of indices from ElasticSearch
curl http://localhost:29200/_aliases

#Create the topic
docker exec -it kafka kafka-topics --zookeeper zookeeper:2181 --create --topic ktopic --partitions 1 --replication-factor 1

# Query 
 curl localhost:29200/estopic/_search | jq


confluent local produce ktopics2 -- --value-format avro --property value.schema='{"type":"record","name":"myrecord","fields":[{"name":"f1","type":"string"}]}'


curl -s -i -X PUT -H  "Content-Type:application/json" \
    http://localhost:8083/connectors/sink-elastic-01/config \
    -d '{
            "connector.class": "io.confluent.connect.elasticsearch.ElasticsearchSinkConnector",
            "connection.url": "http://elasticsearch7:9200",
            "type.name": "_doc",
            "topics": "sample_topic",
            "key.ignore": "true",
            "schema.ignore": "true"
            }'