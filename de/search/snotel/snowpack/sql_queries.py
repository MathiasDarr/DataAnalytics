basin_table_create = (""" CREATE TABLE IF NOT EXISTS basins(
                            basin_id serial PRIMARY KEY ,
                            basin_name CHAR(20) NOT NULL)
                        """)

location_table_create = ("""CREATE TABLE IF NOT EXISTS locations (
                            location_id SERIAL PRIMARY KEY,
                            location_name CHAR(50) NOT NULL,
                            elevation INT,
                            region_id INT REFERENCES basins(basin_id) 
                            );""")

snowpack_table_create = ("""CREATE TABLE IF NOT EXISTS snowpack (
                            id SERIAL PRIMARY KEY,
                            location_id INT NOT NULL,
                            date DATE NOT NULL,
                            snow_current INT NOT NULL,
                            snow_median INT NOT NULL,
                            snow_pct_median INT NOT NULL,
                            water_current INT NOT NULL,
                            water_avg INT NOT NULL,
                            water_pct_avg INT NOT NULL
                            );""")
basin_aggregate_table_create = (
                    """
                    CREATE TABLE IF NOT EXISTS basins_aggregate (
                            region INT NOT NULL,
                            pct_median INT,
                            pct_avg INT, 
                            date DATE NOT NULL);""")

basinID_select = ("""SELECT  basin_id 
                  FROM basins
                  WHERE basins.basin_name = %s;""")

basins_table_insert = ("""INSERT INTO basins (basin_name) VALUES (%s) RETURNING basin_id;""")
location_table_insert = ("""INSERT INTO locations (location_name, elevation, region_id) VALUES (%s, %s, %s);""")
snowpack_table_insert = ("""INSERT INTO snowpack (location_id, date, snow_current, snow_median, snow_pct_median, water_current, water_avg, water_pct_avg )  VALUES (%s, %s, %s, %s, %s, %s, %s, %s);""")


date_table_create = ("""CREATE TABLE IF NOT EXISTS date_table (
                            id SERIAL PRIMARY KEY,
                            date DATE NOT NULL,
                            );""")
insert_date = ("""INSERT INTO date_table (date) VALUES (%s);""")