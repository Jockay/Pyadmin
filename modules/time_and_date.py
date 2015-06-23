__author__ = 'jockay'

 #import arrow
import sys
import os

#print "{0}:{1}".format(arrow.now().time().hour, arrow.now().time().minute)

# HH:MM YYYY-MM-DD
def set_time_and_date(date="", time=""):
    if(not(date == "")):
        os.system('date -s {} 2> time_date_message'.format(date))
    if(not(time == "")):
        os.system('date -s {} 2> time_date_message'.format(time))


if __name__ == '__main__':
    time = ""
    date = ""
    if(len(sys.argv) >= 2):
        date = sys.argv[1]
    if(len(sys.argv) >= 3):
        time = sys.argv[2]
    set_time_and_date(date, time)