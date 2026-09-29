# Data Modeling and ETL with PostgreSQL

## Project Overview

This project builds a PostgreSQL analytics database for Sparkify, a music streaming application. Raw song metadata and user activity logs are transformed from JSON files into a relational star schema designed for song-play analysis.

The project includes database creation, table definitions, SQL insert statements, and a Python ETL pipeline.

## Technologies Used

- Python
- PostgreSQL
- SQL
- pandas
- psycopg2
- Jupyter Notebook
- JSON

## Database Design

The database uses a **star schema** with one fact table and four dimension tables.

### Fact Table

**songplays**

Stores individual song-play events.

| Column | Description |
|---|---|
| songplay_id | Unique song-play identifier |
| start_time | Timestamp of the song play |
| user_id | User identifier |
| level | User subscription level |
| song_id | Song identifier |
| artist_id | Artist identifier |
| session_id | Session identifier |
| location | User location |
| user_agent | User-agent information |

### Dimension Tables

**users**

Stores user account information.

**songs**

Stores song metadata.

**artists**

Stores artist information.

**time**

Breaks song-play timestamps into hour, day, week, month, year, and weekday fields for time-based analysis.

## ETL Pipeline

### 1. Database Creation

`create_tables.py` connects to PostgreSQL, recreates the `sparkifydb` database, drops existing project tables, and creates the required fact and dimension tables.

### 2. Song Data

The ETL pipeline reads JSON files from `data/song_data`.

Each song file is used to populate:

- `songs`
- `artists`

### 3. Log Data

User activity logs are loaded from `data/log_data`.

The pipeline filters the records to events where:

```text
page == "NextSong"
```

Those records are used to populate:

- `time`
- `users`
- `songplays`

### 4. Song and Artist Matching

For each song-play event, the pipeline searches the `songs` and `artists` tables using the song title, artist name, and song duration.

Matching identifiers are then stored in the `songplays` fact table.

## Database Schema

```text
                     users
                       |
                       |
                       |
songs ----------- songplays ----------- artists
                       |
                       |
                       |
                      time
```

The `songplays` table acts as the central fact table, with user, song, artist, and time data stored in separate dimension tables.

See [`SCHEMA.md`](SCHEMA.md) for the table fields.

## Project Structure

```text
data-modeling-etl-postgresql/
│
├── README.md
├── SCHEMA.md
│
├── notebooks/
│   └── etl_development.ipynb
│
├── src/
│   ├── __init__.py
│   ├── create_tables.py
│   ├── etl.py
│   └── sql_queries.py
│
├── data/
│   └── README.md
│
├── requirements.txt
└── .gitignore
```

## Running the Project

Install the required packages:

```bash
pip install -r requirements.txt
```

Make sure PostgreSQL is running and the expected source JSON data is available under `data/song_data` and `data/log_data`.

Create the database and tables:

```bash
python src/create_tables.py
```

Run the ETL pipeline:

```bash
python src/etl.py
```

## Skills Demonstrated

- Relational data modeling
- Star schema design
- Fact and dimension tables
- PostgreSQL database creation
- SQL DDL and DML
- Python ETL development
- JSON ingestion
- Data transformation with pandas
- Database interaction with psycopg2
- Primary keys and conflict handling
- SQL joins
- Modular Python development
