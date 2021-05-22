import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """
    - Creates and connects to the sparkifydb
    - Returns the connection and cursor to sparkifydb
    """
    
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    
    #drop_table_queries = ["DROP TABLE IF EXISTS Fact_Song_Plays;","DROP TABLE Dim_Users;","DROP TABLE IF EXISTS Dim_Songs;","DROP TABLE IF EXISTS Dim_Artists;","DROP TABLE IF EXISTS Dim_Time"]
    
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    
    #create_table_queries = ["CREATE TABLE IF NOT EXISTS Fact_Song_Plays (songplay_id int, start_time timestamp, user_id int, level varchar, song_id varchar, artist_id varchar, session_id int, location varchar, user_agent varchar, PRIMARY KEY (songplay_id));","CREATE TABLE IF NOT EXISTS Dim_Users (user_id int, first_name varchar, last_name vachar, gender vachar, level varchar, PRIMARY KEY (user_id));","CREATE TABLE IF NOT EXISTS Dim_Songs (song_id varchar, title varchar, artist_id varchar, year int, duration numeric, PRIMARY KEY (song_id));","CREATE TABLE IF NOT EXISTS Dim_Artists (artist_id varchar, name varchar, location varchar, latitude numeric, longitude numeric, PRIMARY KEY (artist_id));","CREATE TABLE IF NOT EXISTS Dim_Time (start_time timestamp, hour time, day int, week int, month int, year int, weekday int, PRIMARY KEY (timestamp));"]
    
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    - Drops (if exists) and Creates the sparkify database. 
    
    - Establishes connection with the sparkify database and gets
    cursor to it.  
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()