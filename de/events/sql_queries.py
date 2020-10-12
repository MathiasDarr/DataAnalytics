create_trip_report_table = (""" CREATE TABLE IF NOT EXISTS trip_reports(
                            trip_id serial PRIMARY KEY ,
                            trip_name VARCHAR NOT NULL,
                            trip_report VARCHAR NOT NULL,
                            elevationGain float NOT NULL,
                            mileage INT NOT NUll,
                            trip_date DATE NOT NULL,
                            locations text[] NOT NULL);                                                    
                        """)

trip_location =(""" CREATE TABLE IF NOT EXISTS geographic_location(
                            elevation INT NOT NULL,
                            lat INT NOT NULL,
                            lng INT NOT NULL,
                            location_name VARCHAR NOT NULL,
                            terrain_features text[], 
                            water_availability bool);
                        """)

#
#
trip_report_table_insert = ("""INSERT INTO trip_reports (trip_name, trip_report, elevationGain, mileage, locations, trip_date) VALUES (%s, %s, %s, %s, %s, %s);""")
