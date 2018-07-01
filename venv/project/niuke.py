#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# string = ""
# fizz = "Fizz"
# buzz = "Buzz"
# fizzbuzz = "FizzBuzz"
#
# # print("1,")
# for i in range(1,101):
#     if(i % 15 == 0):
#         string += fizzbuzz + ","
#     elif (i % 3 == 0):
#         string += fizz + ","
#     elif (i % 5 == 0):
#         string += buzz + ","
#     else:
#         string += str(i) + ","
# print(string)
import re

# 用户
str = "U123"
#print(re.match("U[0-9]*$", str))

# 日期
date = "2016-06-02"

# 时间段
# time = "20:00~22:00"
# match = re.match("^\d{2}:d{2}~^\d{2}:d{2}$",time)
# print(match.group())
# 场地

from collections import defaultdict

time = defaultdict(list)
time["a"].