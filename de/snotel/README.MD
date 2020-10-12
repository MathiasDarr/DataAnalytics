## Snotel data pipeline

# Install the Debezium connector
docker exec connect confluent-hub install debezium/debezium-connector-postgresql:0.9.4




Performing streams analysis

curl -i -X POST -H "Accept:application/json" -H  "Content-Type:application/json" http://localhost:8083/connectors/ -d @connectors/snowpack.json
curl -i -X POST -H "Accept:application/json" -H  "Content-Type:application/json" http://localhost:8083/connectors/ -d @connectors/es.json

# 

curl -i -X POST -H "Accept:application/json" -H  "Content-Type:application/json" http://localhost:8083/connectors/ -d @connectors/snowpack_connector.json
curl -i -X POST -H "Accept:application/json" -H  "Content-Type:application/json" http://localhost:8083/connectors/ -d @connectors/inventory.json

Delete a connector
curl -X DELETE localhost:8083/connectors/customers-connector/product

# Console consumer
confluent local consume dbserver.inventory.customer -- --value-format avro --from-beginning --property print.key=true

# List the topics 
kafka-topics --list --zookeeper localhost:2181


# list all schema in psql
SELECT schema_name FROM information_schema.schemata



curl -i -X POST -H  http://localhost:8083/connectors/ -d @connectors/snowpack_connector.json



docker cp connectors/confluentinc-kafka-connect-elasticsearch-5.4.1/lib  snotel_connect_1_c16a92c48224:/kafka/connect/


# -> List the available plugins
curl localhost:8083/connector-plugins/




ES connector 

    "transforms": "unwrap,key",
    "transforms.unwrap.type": "io.debezium.transforms.UnwrapFromEnvelope",
    "transforms.key.type": "org.apache.kafka.connect.transforms.ExtractField$Key",
    "transforms.key.field": "id",
      "key.ignore": "false",
    "type.name": "customer",

    "key.converter": "io.confluent.connect.avro.AvroConverter",
    "key.converter.schema.registry.url": "http://schema-registry:8081",
    "value.converter": "io.confluent.connect.avro.AvroConverter",
    "value.converter.schema.registry.url": "http://schema-registry:8081",
    "schema.ignore": true

