#!/bin/bash
docker exec -it db psql 'dbname=customersDB user=postgres options=--search_path=inventory'