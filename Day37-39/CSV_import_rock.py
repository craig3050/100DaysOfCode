import os
import csv
import collections
from typing import List

data = []

Record = collections.namedtuple(
    'Record',
    'song_name_raw,song_name_clean,artist_name_raw,artist_name_clean,'
    'callsign,song_time,unique_id,combined_name,first_song_in_album'
    # 'SONG_RAW,Song_Clean,ARTIST_RAW,ARTIST_CLEAN,CALLSIGN,TIME,UNIQUE_ID,COMBINED,First'
)


def init():
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'classic-rock-raw-data.csv')

    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        data.clear()
        for row in reader:
            record = parse_row(row)
            data.append(record)

    # print(data)


def parse_row(row):
    # row['SONG_RAW'] = row['SONG_RAW']
    # row['Song_Clean'] = row['Song_Clean']
    # row['ARTIST_RAW'] = row['ARTIST_RAW']
    # row['ARTIST_CLEAN'] = row['ARTIST_CLEAN']
    # row['CALLSIGN'] = row['CALLSIGN']
    # row['TIME'] = int(row['TIME'])
    # row['UNIQUE_ID'] = row['UNIQUE_ID']
    # row['COMBINED'] = row['COMBINED']
    # row['First'] = int(row['First'])


    # row['SONG_RAW'] = row['SONG_RAW']
    # row['song_name_clean'] = row['Song_Clean']
    # row['artist_name_raw'] = row['ARTIST_RAW']
    # row['artist_name_clean'] = row['ARTIST_CLEAN']
    # row['callsign'] = row['CALLSIGN']
    # row['song_time'] = int(row['TIME'])
    # row['unique_id'] = row['UNIQUE_ID']
    # row['combined_name'] = row['COMBINED']
    # row['first_song_in_album'] = int(row['First'])

    record = Record(
        song_name_raw=row.get('SONG_RAW'),
        song_name_clean=row.get('Song_Clean'),
        artist_name_clean=row.get('ARTIST_CLEAN'),
        artist_name_raw=row.get('ARTIST_RAW'),
        callsign=row.get('CALLSIGN'),
        song_time=row.get('TIME'),
        unique_id=row.get('UNIQUE_ID'),
        combined_name=row.get('COMBINED'),
        first_song_in_album=row.get('First')
    )

    return record
