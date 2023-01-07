# Counting Sundays
# Problem 19
# https://projecteuler.net/problem=19

# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4,
# but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during
# the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# Answer: 171.

import datetime

start_date = datetime.datetime(1901, 1, 1)

end_date = datetime.datetime(2000, 12, 31)

# delta time
delta = datetime.timedelta(days=1)

count: int = 0
while (start_date <= end_date):
    if start_date.weekday() == 6 and start_date.date().day == 1:
        count += 1
    start_date += delta

print("Answer - ", count)
