# -*- coding: utf-8 -*-
from datetime import datetime
import re

test_str = 'U003 2018-05-32 8000:00~22:00 A'


def parse(input_str):
    split_book_list = input_str.split(' ')
    booking_time = split_book_list[2]
    match_time = re.match("(?P<start_time>\d{1,2}):00~(?P<end_time>\d{1,2}):00", booking_time)
    print(match_time)
    if match_time != None:
        start_time = match_time.group(1)
        end_time = match_time.group(2)
        print(start_time)
        print(end_time)

    # if len(split_book_list) < 4 or len(split_book_list) > 5:
    #     print('invalid input!')
    #     return
    # # y, m, d = date.split('-')
    # user_id, booking_date, booking_time, court_id = split_book_list
    # start_time, end_time = booking_time.split('~')
    # try:
    #     date = datetime.strptime(booking_date, '%Y-%m-%d')
    #     seven_days = date.weekday()
    # except:
    #     seven_days = 0

    # book_info_dict = {'user_id': user_id,
    #         'booking_date': booking_date,
    #         'booking_time': booking_time,
    #         'start_time': start_time[:3],
    #         'end_time': end_time[:3],
    #         'seven_days': seven_days}
    # return book_info_dict

parse(test_str)
# test = parse(test_str)
# print(test)
