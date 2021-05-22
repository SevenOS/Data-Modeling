# Project: Data Modeling with Postgres

> By Erick Oliveira da Silva, 21 February 2021

## Introduction
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

## Project Description
In this project, you'll apply what you've learned on data modeling with Postgres and build an ETL pipeline using Python. To complete the project, you will need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

## Song Dataset
The first dataset is a subset of real data from the Million Song Dataset. Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID. For example, here are filepaths to two files in this dataset.

'song_data/A/B/C/TRABCEI128F424C983.json'
'song_data/A/A/B/TRAABJL12903CDCF1A.json'

And below is an example of what a single song file, TRAABJL12903CDCF1A.json, looks like.

{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}

## Log Dataset
The second dataset consists of log files in JSON format generated by this event simulator based on the songs in the dataset above. These simulate activity logs from a music streaming app based on specified configurations.

The log files in the dataset you'll be working with are partitioned by year and month. For example, here are filepaths to two files in this dataset.

'log_data/2018/11/2018-11-12-events.json'
'log_data/2018/11/2018-11-13-events.json'
And below is an example of what the data in a log file, 2018-11-12-events.json, looks like.

![](pictures/log_data.png)

## Files

In addition to the data files, the project includes six files:

1. `test.ipynb` displays the first few rows of each table to let me check my database and my sample queries.
2. `create_tables.py` drops and creates tables. I run this file to reset my tables before each time I run the ETL scripts.
3. `etl.ipynb` reads and processes a single file from song_data and log_data and loads the data into the tables. This notebook contains detailed instructions on the ETL process for each of the tables.
4. `etl.py` reads and processes files from song_data and log_data and loads them into the tables. It's based on my work in the ETL notebook.
5. `sql_queries.py` contains all my sql queries, and is imported into the last three files above.
6. `README.md` then provides an introduction to this project.
7. `pipeline.ipynb` run the entire ETL process.
8. `Dashboard.ipynb` create two simple Dashboards.

## Database Schema for Song Play Analysis

Using the song and log datasets, I created a denormalized star schema using Postgres Database with psycopg2 lib, Python and SQL.
This project is a Data Warehouse optimized for quick consultations and its objective is to answer the questions of where, when, what and how much data are present according to the qualitative and quantitative metrics used.

![](pictures/StarSchema.png)

## ETL Pipeline

Extract, transform, load (ETL) is the general procedure of copying data from one or more sources into a destination system which represents the data differently from, or in a different context than, the sources.

#### Directories

Directories utilized:
- /data/log_data and 
- /data/song_data.

#### Running ETL Pipeline

To recreate and load the Star Schema, i have ben utilized the `create_tables.py`, `sql_queries.py` and the `etl.py`.

The steps to run the pipeline are as follows:

1. Run the `pipeline.ipynb` to recreate the Database and the Star Schema, and load them.
2. Running `test.ipynb` (in a jupyter notebook) confirms that the tables were successfully created with the correct columns.

#### Running Dashboards

To view the Dashboard you need to running the `pipeline.ipynb`.

#### Sample Queries

Get the quantity of songs played and the quantity of user are listening by level and gender: <br>

%sql SELECT COUNT(F.songplay_id) AS Qty_Song_Plays, \
            count(Distinct F.user_id) Qty_Users, \
            F.level, \
            Du.gender \
     FROM Fact_Song_Plays AS F\
     JOIN Dim_users AS Du ON F.user_id = Du.user_id \
     GROUP BY \
             F.level \
             ,Du.gender

![](pictures/query_qty_songs.png)

Get the top 10 quantity of songs played by user: <br>

%sql SELECT COUNT(F.songplay_id) AS song_count, Du.user_id, Du.first_name, Du.last_name \
     FROM Fact_Song_Plays AS F \
          JOIN Dim_users AS Du ON F.user_id = Du.user_id \
     GROUP BY \
             Du.user_id \
             ,Du.first_name \
     ORDER BY COUNT(F.songplay_id) DESC LIMIT 10\

![](pictures/query_qty_songs_by_user.png)