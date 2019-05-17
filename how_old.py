# Script to calculate the age of a user using their birthday
################################################################################

import time
import datetime
import pytz
import logging

logging.basicConfig(level=logging.DEBUG)

datetime_format = '%Y-%m-%d %H:%M:%S'
time_started = time.strftime(datetime_format)

logging.info('script started at ' + str(time_started))


ut = time.strptime('1980.10.21.23.45.00','%Y.%m.%d.%H.%M.%S')

'''
im gonna need an aware date with moscow timezone
>>> v = datetime.datetime.today()
>>> type(v)
<class 'datetime.datetime'>
>>> datetime.date.strftime(v, '%Y.%m.%d.%H.%M.%S')
'2019.05.16.22.42.26'
'''

#finding the time zone the user was born
find_user_tz = input('please write the time zone you where born: ')
def find_tz(find_user_tz):
    #looping throught the list provided by pytz to find the time zone
    for tz in pytz.all_timezones:
        if find_user_tz.lower() in tz.lower():
            print(f'Found this {tz}')
        
    #if the time zone was not found
    print(f'Your time zone "{find_user_tz}" was not found in the list ')
    #TODO maybe add a way to check the list

def get_age():
    print('hi, please tell me when you where born')
    print('format: year month day hour minute')
    print('example: 1900 12 31 23 56')
    age = input()
    return age

#user_age = get_age()
find_tz(user_tz)

logging.info('script finished at ' + str(time_started))


