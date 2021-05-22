# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS Fact_Song_Plays;"
user_table_drop = "DROP TABLE IF EXISTS Dim_Users;"
song_table_drop = "DROP TABLE IF EXISTS Dim_Songs;"
artist_table_drop = "DROP TABLE IF EXISTS Dim_Artists;"
time_table_drop = "DROP TABLE IF EXISTS Dim_Time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS Fact_Song_Plays (
                            songplay_id serial PRIMARY KEY, 
                            start_time bigint NOT NULL, 
                            user_id int NOT NULL,
                            level varchar NOT NULL, 
                            song_id varchar, 
                            artist_id varchar, 
                            session_id int, 
                            location varchar,
                            user_agent varchar,
                            UNIQUE (start_time, user_id));""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS Dim_Users (
                        user_id int NOT NULL, 
                        first_name varchar NOT NULL, 
                        last_name varchar NOT NULL, 
                        gender varchar,
                        level varchar, 
                        PRIMARY KEY (user_id));""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS Dim_Songs (
                        song_id varchar NOT NULL, 
                        title varchar NOT NULL, 
                        artist_id varchar NOT NULL, 
                        year int, 
                        duration numeric NOT NULL, 
                        PRIMARY KEY (song_id));""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS Dim_Artists (
                            artist_id varchar NOT NULL, 
                            name varchar NOT NULL, 
                            location varchar, 
                            latitude numeric, 
                            longitude numeric, 
                            PRIMARY KEY (artist_id));""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS Dim_Time (
                        start_time timestamp NOT NULL, 
                        hour int NOT NULL, 
                        day int NOT NULL, 
                        week int NOT NULL, 
                        month int NOT NULL, 
                        year int NOT NULL, 
                        weekday int NOT NULL, 
                        PRIMARY KEY (start_time));""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO Fact_Song_Plays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                            ON CONFLICT (start_time, user_id) DO UPDATE SET level=EXCLUDED.level,
                                                                    song_id=EXCLUDED.song_id,
                                                                    artist_id=EXCLUDED.artist_id,
                                                                    session_id=EXCLUDED.session_id,
                                                                    location=EXCLUDED.location,
                                                                    user_agent=EXCLUDED.location;""")

user_table_insert = ("""INSERT INTO Dim_Users (user_id, first_name, last_name, gender, level)
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level;""")

song_table_insert = ("""INSERT INTO Dim_Songs (song_id, title, artist_id, year, duration)
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (song_id) DO NOTHING;""")

artist_table_insert = ("""INSERT INTO Dim_Artists (artist_id, name, location, latitude, longitude)
                            VALUES (%s, %s, %s, %s, %s)
                            ON CONFLICT (artist_id) DO NOTHING;""")

time_table_insert = ("""INSERT INTO Dim_Time (start_time, hour, day, week, month, year, weekday)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                        ON CONFLICT (start_time) DO NOTHING;""")

# FIND SONGS

song_select = ("""SELECT  Ds.song_id,
                          Da.artist_id
                  FROM    Dim_Songs AS Ds
                  JOIN    Dim_Artists AS Da ON (Ds.artist_id = Da.artist_id)
                  WHERE   Ds.title = %s 
                          AND Da.name = %s AND 
                          Ds.duration = %s;""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]