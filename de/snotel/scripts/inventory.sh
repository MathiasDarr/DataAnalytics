#!/bin/bash
docker exec -it db psql 'dbname=snowpackDB user=postgres options=--search_path=inventory'