from pipelines.search.snotel.snowpack.run_scraper import extract_snowpack_data
from pipelines.search.snotel.snowpack.sql_queries import basin_table_create, basin_aggregate_table_create,\
    snowpack_table_create, location_table_create, basins_table_insert,location_table_insert
from snotel.postgresConnection import get_postgres_connection


conn = get_postgres_connection()
cur = conn.cursor()
create_table_queries = [ basin_table_create, snowpack_table_create, basin_aggregate_table_create, location_table_create]

for query in create_table_queries:
    cur.execute(query)
conn.commit()

regions_dict = extract_snowpack_data()
regions_dict.pop('year')
regions_dict.pop('day')
regions_dict.pop('month')

# We will start

for region in regions_dict.keys():
    regions_dict[region].pop('Basin Index')
    locations = regions_dict[region].keys()
    cur.execute(basins_table_insert, (region,))
    basin_id  = cur.fetchone()[0]
    conn.commit()
    for location in locations:
        location_dict = regions_dict[region][location]
        elevation = location_dict['Elev (ft) ']
        cur.execute(location_table_insert, (location,elevation,basin_id))
    conn.commit()

conn.close()