# Data Modeling with Postgres

## Project Summary

This project builds a PostgreSQL database for Sparkify, a music streaming startup. The source data consists of JSON files containing song metadata and user activity logs. The goal is to design a star schema optimized for song play analysis and build an ETL pipeline that loads the data into the database.

The project creates one fact table and four dimension tables:

- songplays
- users
- songs
- artists
- time

Python, Pandas, PostgreSQL, and psycopg2 are used to extract the data, transform it into the required format, and load it into the database.

---

## Repository Files

### create_tables.py

Creates the Sparkify database, drops existing tables if they exist, and recreates all required tables.

### sql_queries.py

Contains all SQL statements used throughout the project, including:

- CREATE TABLE
- DROP TABLE
- INSERT
- Song lookup query

### etl.py

Processes every JSON file in both datasets and loads the data into the database.

### etl.ipynb

Notebook used to develop and test the ETL process on individual files before implementing the full pipeline.

### test.ipynb

Verifies that the tables were created correctly and that the ETL pipeline successfully loaded the data.

---

## Database Schema

The database uses a star schema.

### Fact Table

**songplays**

Stores one record for every song play event.

Columns:

- songplay_id
- start_time
- user_id
- level
- song_id
- artist_id
- session_id
- location
- user_agent

### Dimension Tables

**users**

Stores user information.

- user_id
- first_name
- last_name
- gender
- level

**songs**

Stores song information.

- song_id
- title
- artist_id
- year
- duration

**artists**

Stores artist information.

- artist_id
- name
- location
- latitude
- longitude

**time**

Stores timestamp information broken into useful reporting fields.

- start_time
- hour
- day
- week
- month
- year
- weekday

---

## ETL Pipeline

The ETL pipeline processes two datasets.

### Song Dataset

Each song JSON file is read into a Pandas DataFrame.

The pipeline extracts:

- Song information for the songs table
- Artist information for the artists table

### Log Dataset

Each log file is filtered to include only "NextSong" events.

The pipeline:

- Converts timestamps into datetime values
- Builds the time dimension
- Loads user records
- Looks up matching song_id and artist_id
- Inserts records into the songplays fact table

---

## Running the Project

1. Create the database and tables.

```
python create_tables.py
```

2. Run the ETL pipeline.

```
python etl.py
```

3. Verify the results.

Open and run every cell in:

```
test.ipynb
```

---

## Technologies Used

- Python
- PostgreSQL
- Pandas
- psycopg2
- Jupyter Notebook