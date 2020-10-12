#!/bin/bash
confluent local consume $1 -- --from-beginning --property print.key=true