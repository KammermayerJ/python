#!/usr/bin/env python3

import random
import re
import sys
import time

'''

Birthday number generator and validator for CZE

python birthnumber.py ->                Day of the birth [YYYY-MM-DD]: 1995-05-15
                                        Sex [M/F]: F
                                        Generated number is 955515/1375

python birthnumber.py 955515/1375 ->    955515/1375 is valid number for women.
                                        Date of birth day: 15.05.1995

'''

def get_data(num):
    '''
    Get all data from birthcode
    return 4 parameters
    y = year, m = month, d = day, c = checksum
    '''
    date, c = re.split(r'/', num)
    y, m, d = [int(x) for x in re.findall(r'..', date)]
    y = convert_year(y)
    return y, m, d, int(c)

def convert_year(y):
    '''
    Convert year with century.
    return year
    91 -> 1991
    12 -> 2012
    '''
    a, b = [int(x) for x in time.strftime('%y,%Y').split(',')]
    if a > y:
        y = int(b - a + y)
    else:
        y = int(b - a + y - 100)
    return y

def verify_number(num):
    '''
    Verify if birthcode is valid
    '''
    match = re.fullmatch(r'\d{6}/\d{3,4}', num)
    if match:
        y, m, d, c = get_data(match.group())
        if not valid_num(num):
            print('{} is invalid number. Not divisible by 11.'.format(num))
        elif y <= 1953 and len(str(c)) != 3 or y >= 1954 and len(str(c)) != 4:
            print('{} bad checksum number.'.format(num))
        else:
            sex = ['man','women'][int(m) > 12]
            if int(m) > 12: m -= 50
            print('{} is valid number for {}. '.format(num, sex))
            print('Date of birth day: {}.{}.{}'.format(d, m, y))
    else:
        print('Invalid input. (Bad format, should be YYMMDD/CCCC)')

def valid_num(num):
    '''
    Check if birthcode is divisible by 11
    return True or False
    '''
    if '/' in num: num = num.replace('/', '')
    return int(num) % 11 == 0


def generate_number():
    '''
    Generator of birthcode
    '''
    day = input('Day of the birth [YYYY-MM-DD]: ')
    sex = input('Sex [M/F]: ').upper()
    match = re.fullmatch(r'\d{4}-\d{2}-\d{2}', day)
    if match and sex in 'MF':
        y, m, d = day.split('-')
        if sex == 'F':
            m = str(int(m) + 50)
        date = y[2:] + m + d
        num = ''
        while True:
            if int(y) > 1953:
                c = str(random.randint(1000, 10000))
            else:
                c = str(random.randint(100, 1000))
            num = date + '/' + c
            if valid_num(num):
                print('Generated number is:', num)
                break
    else:
        print('Invalid input. ([YYYY-MM-DD] and sex [M/F])')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        verify_number(sys.argv[1])
    else:
        generate_number()
