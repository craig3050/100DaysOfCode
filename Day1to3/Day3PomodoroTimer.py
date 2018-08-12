from datetime import datetime
from datetime import timedelta
from time import sleep

time_counter = input("Please enter the time for the timer in minutes: ")

time_now = datetime.today()
print(time_now)

time_counter = int(time_counter) * 60
print(time_counter)
time_counter = timedelta(seconds = time_counter)
print(time_counter)

while datetime.today() <= (time_now + time_counter):
    #print(datetime.strptime((time_now + time_counter) - datetime.today(), '%H:%M:%S'))
    print((time_now + time_counter) - datetime.today())
    sleep(1)


