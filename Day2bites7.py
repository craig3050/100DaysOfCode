'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime
import os
import urllib.request
import re

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
#logfile = open('log', 'a').close()
logfile = os.path.join('log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()

def convert_to_datetime(line):
    match = re.search(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}', line)
    date = datetime.strptime(match.group(), '%Y-%m-%dT%H:%M:%S') # .strftime('%Y, %m, %d, %H, %M, %S')
    return date
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object. 
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
    pass


def time_between_shutdowns(loglines):
    time_gap = []
    for line in loglines:
        if SHUTDOWN_EVENT in line:
            time_gap.append(convert_to_datetime(line))
    first_time = time_gap[0]
    second_time = time_gap[1]
    output = second_time - first_time
    return output




    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the
       timedelta between the first and last one.
       Return this datetime.timedelta object.'''
    pass


for line in loglines:
    convert_to_datetime(line)

time_between_shutdowns(loglines)
