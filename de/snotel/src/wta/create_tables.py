from wta.sql_queries import create_trip_report_table, trip_location
from utils.postgresConnection import get_postgres_connection
from wta.scrape_WTA import scrape_range

conn = get_postgres_connection('snowpackDB')
cur = conn.cursor()
query = 'CREATE SCHEMA IF NOT EXISTS snowpack;'
params = ('schema_name', 'user_name')
cur.execute(query, params)
conn.commit()

conn = get_postgres_connection('snowpackDB','snowpack')
cur = conn.cursor()
create_table_queries = [create_trip_report_table, trip_location]

for query in create_table_queries:
    cur.execute(query)
conn.commit()

scrape_range(0,1)