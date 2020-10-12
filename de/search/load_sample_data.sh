#!/bin/bash 

#kafkacat -b localhost:9092 -t sample_topic -P -T -l ./data/dummy_data.kcat

kafkacat -b localhost:9092 -t est -P -T -l ./data/trial.json
