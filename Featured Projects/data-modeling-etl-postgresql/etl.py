import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """
    Reads one song JSON file and inserts its song and artist records.
    """
    df = pd.read_json(filepath, lines=True)

    song_data = df[
        ['song_id', 'title', 'artist_id', 'year', 'duration']
    ].values[0].tolist()

    cur.execute(song_table_insert, song_data)

    artist_data = df[
        [
            'artist_id',
            'artist_name',
            'artist_location',
            'artist_latitude',
            'artist_longitude'
        ]
    ].values[0].tolist()

    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
    Reads one log JSON file and inserts time, user, and songplay records.
    """
    df = pd.read_json(filepath, lines=True)

    df = df[df['page'] == 'NextSong']

    t = pd.to_datetime(df['ts'], unit='ms')

    time_data = (
        t,
        t.dt.hour,
        t.dt.day,
        t.dt.week,
        t.dt.month,
        t.dt.year,
        t.dt.weekday
    )

    column_labels = (
        'start_time',
        'hour',
        'day',
        'week',
        'month',
        'year',
        'weekday'
    )

    time_df = pd.DataFrame(dict(zip(column_labels, time_data)))

    for _, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    user_df = df[
        ['userId', 'firstName', 'lastName', 'gender', 'level']
    ]

    for _, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    for _, row in df.iterrows():
        cur.execute(
            song_select,
            (row.song, row.artist, row.length)
        )

        results = cur.fetchone()

        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        songplay_data = (
            pd.to_datetime(row.ts, unit='ms'),
            int(row.userId),
            row.level,
            songid,
            artistid,
            int(row.sessionId),
            row.location,
            row.userAgent
        )

        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """
    Finds every JSON file in a directory and processes each file.
    """
    all_files = []

    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))

        for file in files:
            all_files.append(os.path.abspath(file))

    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    for index, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(index, num_files))


def main():
    """
    Connects to Sparkify, processes both datasets, and closes the connection.
    """
    conn = psycopg2.connect(
        "host=127.0.0.1 "
        "dbname=sparkifydb "
        "user=student "
        "password=student"
    )

    cur = conn.cursor()

    process_data(
        cur,
        conn,
        filepath='data/song_data',
        func=process_song_file
    )

    process_data(
        cur,
        conn,
        filepath='data/log_data',
        func=process_log_file
    )

    conn.close()


if __name__ == "__main__":
    main()