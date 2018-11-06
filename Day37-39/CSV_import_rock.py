import os
import csv
import collections
from typing import List

data = []

Record = collections.namedtuple(
    'Record',
    'SONG_RAW,Song_Clean,ARTIST_RAW,ARTIST_CLEAN,CALLSIGN,TIME,UNIQUE_ID,COMBINED,First',

)


def init():
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'classic-rock-raw-data.csv')

    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        # for row in reader:
        #     print(f'row = {row}')

        data.clear()
        for row in reader:
            record = parse_row(row)
            data.append(record)


def parse_row(row):
    row['SONG_RAW'] = row['song_name_raw']
    row['Song_Clean'] = row['song_name_clean']
    row['ARTIST_RAW'] = row['artist_name_raw']
    row['ARTIST_CLEAN'] = row['artist_name_clean']
    row['CALLSIGN'] = row['callsign']
    row['TIME'] = row['song_time']
    row['UNIQUE_ID'] = int(row['unique_id'])
    row['COMBINED'] = row['combined_name']
    row['First'] = int(row['first_song_in_album'])

    record = Record(
        **row
    )

    return record
