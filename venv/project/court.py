#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import re
import time
from collections import defaultdict

class Court(object):
    def __init__(self):
        # self.id
        self.time = defaultdict(list)
        self.orderded_list = []
        self.price_five = [0] * 22
        self.price_two = [0] * 22
        # 周内价格初始化
        self.price_five[9] = 30
        self.price_five[10] = 30
        self.price_five[11] = 30
        self.price_five[12] = 50
        self.price_five[13] = 50
        self.price_five[14] = 50
        self.price_five[15] = 50
        self.price_five[16] = 50
        self.price_five[17] = 50
        self.price_five[18] = 80
        self.price_five[19] = 80
        self.price_five[20] = 60
        self.price_five[21] = 60
        # 周末价格初始化
        self.price_two[9] = 40
        self.price_two[10] = 40
        self.price_two[11] = 40
        self.price_two[12] = 50
        self.price_two[13] = 50
        self.price_two[14] = 50
        self.price_two[15] = 50
        self.price_two[16] = 50
        self.price_two[17] = 50
        self.price_two[18] = 60
        self.price_two[19] = 60
        self.price_two[20] = 60
        self.price_two[21] = 60

    def find_conflict(self, booking_date, start_time, end_time):
        if booking_date not in self.time.keys():
            return True
        else:
            for index in range(0,len(self.time[booking_date])):
                #print(self.time[booking_date])
                hour = self.time[booking_date][index]
                #print(hour)
                #print(type(hour))
                begin = hour[0]
                end = hour[1]
                if ((end_time > begin and end_time < end) or (start_time >= begin and start_time <= end) or (
                        start_time < begin and end_time > end)):
                    return False
            return True

    def book(self, book_info_list):
        date = book_info_list["booking_date"]
        if book_info_list["booking_date"] not in self.time.keys():
            self.time[date].append((book_info_list["start_time"], book_info_list["end_time"]))
        else:
            self.time[date].append((book_info_list["start_time"], book_info_list["end_time"]))

        # print(self.time[date])
        if book_info_list["seven_days"] >= 1 and book_info_list["seven_days"] <= 5:
            price_days = 1
        else:
            price_days = 6

        profit = 0
        for i in range(book_info_list["start_time"], book_info_list["end_time"]):
            if price_days == 1:
                profit += self.price_five[i]
            elif price_days == 6:
                profit += self.price_two[i]

        book_record = {'booking_date': book_info_list["booking_date"],
                       'booking_time': book_info_list["booking_time"],
                       'profit': profit}
        self.orderded_list.append(book_record)

    def cancel(self):
        pass

    def output(self):
        pass