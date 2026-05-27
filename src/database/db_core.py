from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

class CassandraProvider:
    def __init__(self):
        self.cluster = None
        self.session = None

    def connect(self):
        self.cluster = Cluster(['cassandra-node1', 'cassandra-node2'])
        self.session = self.cluster.connect()

        self.session.execute("""
                    CREATE KEYSPACE IF NOT EXISTS url_shortener 
                    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 2};
                    """)

        self.session.set_keyspace('url_shortener')

        self.session.execute("""
            CREATE TABLE IF NOT EXISTS urls (
            short_url text PRIMARY KEY,
            original_url text,
            created_at timestamp,
            last_used_at timestamp);
        """)

    def close(self):
        if self.cluster:
            self.cluster.shutdown()

db_provider = CassandraProvider()
db_provider.connect()

def get_db():
    return db_provider.session