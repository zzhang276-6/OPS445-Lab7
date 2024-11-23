#!/usr/bin/env python3
# Student ID: zzhang276
from lab7d import *

t1 = Time(8, 0, 0)
t2 = Time(8, 55, 0)
t3 = Time(9, 50, 0)

td = Time(0, 50, 0)

tsum1 = t1.sum_times(td)
tsum2 = t2.sum_times(td)
t3.change_time(1800) 

print(t1.format_time(), '+', td.format_time(), '-->', tsum1.format_time())
print(t2.format_time(), '+', td.format_time(), '-->', tsum2.format_time())
print('09:50:00 + 1800 sec -->', t3.format_time())
