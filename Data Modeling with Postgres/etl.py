import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    '''
    Execute the insert into Dim_Songs and Dim_Artists.

            Parameters:
                    cur: A database cursor.
                    filepath (string): The file path.
    '''
    df = pd.read_json(filepath, lines=True)

    filter_col = ['song_id','title','artist_id','year','duration']
    song_data = df[filter_col].values[0].tolist()
    cur.execute(song_table_insert, song_data)
    
    filter_col = ['artist_id','artist_name','artist_location','artist_latitude','artist_longitude']
    artist_data = df[filter_col].values[0].tolist()
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    '''
    Execute the insert into Dim_Time, Dim_Users and Fact_Song_Plays.
    - Filter DataFrame and transform the unix time into DateTime and create other fields using the date and insert into the Dim_Time.
    - Insert into the Dim_Users.
    - Filter by title, name and duration and insert into the Fact_Song_Plays.
    
            Parameters:
                    cur: A database cursor.
                    filepath (string): The file path.
    '''    
    df = pd.read_json(filepath, lines=True) 

    df = df[df['page'] == 'NextSong']

    t = pd.to_datetime(df['ts'], unit='ms')
    
    time_data = [t, t.dt.hour, t.dt.day, t.dt.week, t.dt.month, t.dt.year, t.dt.weekday]
    column_labels = ('start_time', 'hour', 'day', 'week', 'month', 'year', 'weekday')
    time_df = pd.DataFrame.from_dict(dict(zip(column_labels, time_data)))

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    filter_col = ['userId', 'firstName', 'lastName', 'gender', 'level']
    user_df = df[filter_col]

    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    for index, row in df.iterrows():
        
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        songplay_data = (row.ts, row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    '''
    Execute the data process to extract, transform and load all data.
    - Find all '.json' files
    - Count the amount of '.json' files.
    - Process each file.

            Parameters:
                    cur: A database cursor.
                    conn (string): The String connectio to the Database.
                    filepath (string): The file path.
                    func: The function to execute the process. 
    '''    
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    """
    - Establishes connection with the sparkify database and gets
    cursor to it.  
    - Set the parameters to execute the function process_song_file.  
    - Set the parameters to execute the function process_log_file.  
    - Finally, closes the connection. 
    """
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()