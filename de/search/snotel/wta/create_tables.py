from pipelines.search.snotel.wta.sql_queries import create_trip_report_table, trip_location
from pipelines.search.snotel.postgresConnection import get_postgres_connection


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