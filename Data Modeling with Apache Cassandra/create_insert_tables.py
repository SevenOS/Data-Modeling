import cassandra
import csv
from sql_queries import create_table_queries, drop_table_queries, create_keyspace, \
                        session_history_insert, user_by_session_insert, user_by_song_insert

def create_database():
    """
    - Create a Cluster and Connection to Database
    - Create Keyspace
    - Set Keyspace
    - Return the connectios
    """
    
    from cassandra.cluster import Cluster
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    
    try:
        session.execute(create_keyspace)
    except Exception as e:
        print(e)
    
    try:
        session.set_keyspace('sparkifydb')
    except Exception as e:
        print(e)
    
    return cluster, session


def drop_tables(cluster, session):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """     
    for query in drop_table_queries:
        session.execute(query)

def create_tables(cluster, session):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    for query in create_table_queries:
        session.execute(query)

def insert_tables(cluster, session, file='event_datafile_new.csv'):
    """
    Insert into all tables.    
    """
    with open(file, encoding = 'utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader) 
        for line in csvreader:
            session.execute(session_history_insert, 
                            (int(line[8]), int(line[3]), line[0], line[9], float(line[5])))
    
    
    with open(file, encoding = 'utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader)
        for line in csvreader:
            session.execute(user_by_session_insert, 
                            (int(line[10]), int(line[8]), int(line[3]), line[0], line[9], line[1] , line[4]))
    
    with open(file, encoding = 'utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader)
        for line in csvreader:
            session.execute(user_by_song_insert, 
                            (line[9], int(line[10]), line[1], line[4]))
    
def main():
    """
    - Creates if exists the sparkify database. 
    - Establishes connection with the sparkify database and gets
    conection to it.  
    - Drops all the tables.  
    - Creates all tables needed. 
    """
    cluster, session = create_database()
    
    drop_tables(cluster, session)
    create_tables(cluster, session)
    insert_tables(cluster, session, file='event_datafile_new.csv')

if __name__ == "__main__":
    main()