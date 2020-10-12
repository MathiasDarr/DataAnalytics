curl -i -X POST -H "Accept:application/json" -H  "Content-Type:application/json" http://localhost:8083/connectors/ -d @connectors/inventory.json


The confluent image of connect has confluent-hub installed thankfully
confluent-hub install --no-prompt debezium/debezium-connector-postgresql:0.9.4