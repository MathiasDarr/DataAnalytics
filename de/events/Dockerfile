FROM confluentinc/cp-kafka-connect-base:5.4.1

COPY target/components/packages/my-connector-5.4.1.zip /tmp/my-connector-5.4.1.zip

RUN confluent-hub install --no-prompt debezium/debezium-connector-postgresql:0.9.4