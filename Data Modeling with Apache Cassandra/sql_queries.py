### CREATE KEYSPACE ###
create_keyspace = (""" CREATE KEYSPACE IF NOT EXISTS sparkifydb 
                        WITH REPLICATION = 
                        { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }""")


### DROP TABLES ###

session_history_drop = "DROP TABLE IF EXISTS session_history;"
user_by_session_drop    = "DROP TABLE IF EXISTS user_by_session;"
user_by_song_drop    = "DROP TABLE IF EXISTS user_by_song;"


### CREATE TABLES ###

# Session Table with 2 Partition Keys (sessionId, itemInSession) to include in the WHERE statement
session_history_create = ("""CREATE TABLE IF NOT EXISTS session_history (
                              session_id int, item_in_session int, artist text, song text, length float,
                              PRIMARY KEY (session_id, item_in_session));""")

# User Table with 2 Partion Keys (userId, sessionId) to include in the WHERE statement ...
# ... and 1 Clustering Key (itemInSession) to order songs by
user_by_session_create = ("""CREATE TABLE IF NOT EXISTS user_by_session (
                          user_id int, session_id int, item_in_session int, artist text, song text, first_name text, last_name text,
                          PRIMARY KEY ((user_id, session_id), item_in_session));""")

# Song Table with 1 Partition Key (song) to include in the WHERE statement ...
# ... and 1 Clustering Key (userId) to make the Partition Key unique
user_by_song_create = ("""CREATE TABLE IF NOT EXISTS user_by_song (
                          song text, user_id int, first_name text, last_name text,  
                          PRIMARY KEY ((song), user_id));""")


### INSERT RECORDS ###

session_history_insert = ("""INSERT INTO session_history (session_id, item_in_session, artist, song, length)
                           VALUES (%s, %s, %s, %s, %s);""")

user_by_session_insert = ("""INSERT INTO user_by_session (user_id, session_id, item_in_session, artist, song, first_name, last_name)
                        VALUES (%s, %s, %s, %s, %s, %s, %s);""")

user_by_song_insert = ("""INSERT INTO user_by_song (song, user_id, first_name, last_name)
                        VALUES (%s, %s, %s, %s);""")


### SELECT STATEMENTS ###

session_history_select = ("""SELECT artist, song, length FROM session_history WHERE session_id = %s AND item_in_session = %s;""")

user_by_session_select = ("""SELECT artist, song, item_in_session, first_name, last_name FROM user_by_session WHERE user_id = %s AND session_id = %s;""")

user_by_song_select = ("""SELECT first_name, last_name, user_id, song FROM user_by_song WHERE song=%s;""")

# QUERY LISTS

create_table_queries = [session_history_create, user_by_session_create, user_by_song_create]
drop_table_queries = [session_history_drop, user_by_session_drop, user_by_song_drop]
insert_table_queries = [session_history_insert, user_by_session_insert, user_by_song_insert]