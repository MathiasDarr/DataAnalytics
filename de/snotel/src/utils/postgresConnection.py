import psycopg2

def get_postgres_connection(db, schema = None):
    conn = psycopg2.connect("host=localhost dbname={} user=postgres password=postgres".format(db)) if not schema else \
        psycopg2.connect(host="localhost", port="5432", user="postgres",  password="postgres", database=db, options="-c search_path={}".format(schema))
    return conn;


# psycopg2.connect(host="localhost",
#                  port="5432",
#                  user="postgres",
#                  password="postgres",
#                  database="snowpackDB",
#                  options="-c search_path=snowpack")