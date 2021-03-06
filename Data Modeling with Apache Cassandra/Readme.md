# Project: Data Modeling with Cassandra

> By Erick Oliveira da Silva, 26 February 2021

## Introduction
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analysis team is particularly interested in understanding what songs users are listening to. Currently, there is no easy way to query the data to generate the results, since the data reside in a directory of CSV files on user activity on the app.

They'd like a data engineer to create an Apache Cassandra database which can create queries on song play data to answer the questions, and wish to bring you on the project. Your role is to create a database for this analysis. You'll be able to test your database by running queries given to you by the analytics team from Sparkify to create the results.

## Project Description
In this project, you'll apply what you've learned on data modeling with Apache Cassandra and complete an ETL pipeline using Python. To complete the project, you will need to model your data by creating tables in Apache Cassandra to run queries. You are provided with part of the ETL pipeline that transfers data from a set of CSV files within a directory to create a streamlined CSV file to model and insert data into Apache Cassandra tables.

We have provided you with a project template that takes care of all the imports and provides a structure for ETL pipeline you'd need to process this data.

## Datasets
For this project, you'll be working with one dataset: event_data. The directory of CSV files partitioned by date. Here are examples of filepaths to two files in the dataset:
    event_data/2018-11-08-events.csv
    event_data/2018-11-09-events.csv

## Project Template
To get started with the project, go to the workspace on the next page, where you'll find the project template (a Jupyter notebook file). You can work on your project and submit your work through this workspace.

The project template includes one Jupyter Notebook file, in which:

you will process the event_datafile_new.csv dataset to create a denormalized dataset
you will model the data tables keeping in mind the queries you need to run
you have been provided queries that you will need to model your data tables for
you will load the data into tables you create in Apache Cassandra and run your queries

## Project Steps
Below are steps you can follow to complete each component of this project.

Modeling your NoSQL database or Apache Cassandra database
1. Design tables to answer the queries outlined in the project template
2. Write Apache Cassandra CREATE KEYSPACE and SET KEYSPACE statements
3. Develop your CREATE statement for each of the tables to address each question
4. Load the data with INSERT statement for each of the tables
5. Include IF NOT EXISTS clauses in your CREATE statements to create tables only if the tables do not already exist. We recommend you also include DROP TABLE statement for each table, this way you can run drop and create tables whenever you want to reset your database and test your ETL pipeline
6. Test by running the proper select statements with the correct WHERE clause

## Files

In addition to the data files, the project includes six files:

1. `event_datafile_new.csv` the output file generate to the Processing_Checks notebook.
2. `create_insert_tables.py` drops, creates and insert tables. I run this file to reset my tables before each time I run the ETL scripts.
3. `Project_1B_ Project_Template.ipynb` reads and processes the entire template etl.
4. `Processing_Checks.py` reads and processes files from event_data and generete the output csv.
5. `sql_queries.py` contains all my sql queries, and is imported into the last three files above.
6. `README.md` then provides an introduction to this project.
7. `Processing_Checks.ipynb` contais the process to generate the output file and data checks, to validate the input and the output data.
8. `Pipeline.ipynb` run the entire ETL process.


## ETL Pipeline

Extract, transform, load (ETL) is the general procedure of copying data from one or more sources into a destination system which represents the data differently from, or in a different context than, the sources.

#### Directories

Directories utilized:
- /event_data/

#### Running ETL Pipeline

To recreate and load the Star Schema, i have ben utilized the `create_tables.py`, `sql_queries.py` and the `etl.py`.

The steps to run the pipeline are as follows:

1. Run the `pipeline.ipynb` to process the files, recreate the Database, and load them, and run the queries.