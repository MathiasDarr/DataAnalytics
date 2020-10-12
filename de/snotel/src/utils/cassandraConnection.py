# This should make a connection to a Cassandra instance your local machine
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

def createCassandraConnection():
    auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')
    conn = ["127.0.0.1"]
    try:
        cluster = Cluster(["127.0.0.1"], auth_provider=auth_provider)

        # To establish connection and begin executing queries, need a session
        session = cluster.connect()
        return session
    except Exception as e:
        print(e)
        return None

def createKeySpace(keyspace_name, session):
    # Create a Keyspace
    try:
        session.execute("CREATE KEYSPACE IF NOT EXISTS " + keyspace_name + " WITH REPLICATION =  { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }")
    except Exception as e:
        print(e)

