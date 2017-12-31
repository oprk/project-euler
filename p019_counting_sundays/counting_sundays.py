# Counting Sundays
#
# You are given the following information, but you may prefer to do some
# research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
#
# A leap year occurs on any year evenly divisible by 4, but not on a century
# unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century
# (1 Jan 1901 to 31 Dec 2000)?

import time

def is_leap_year(year):
  return ((year % 100 == 0) and (year % 400 == 0) or
          (year % 100 != 0) and (year % 4 == 0))

# Use 1-index based numbering system for months.
# February is 2, etc.
def days_in_month(year, month):
  if month == 2:
    return 29 if is_leap_year(year) else 28
  elif month in (4, 6, 9, 11):
    return 30
  else:
    return 31

def days_in_year(year):
  return 366 if is_leap_year(year) else 365

# Test not-leap year.
assert days_in_year(1991) == 365
assert sum(days_in_month(1991, month) for month in xrange(1, 13)) == 365
# Test leap year.
assert days_in_year(2000) == 366
assert days_in_year(1988) == 366
assert sum(days_in_month(2000, month) for month in xrange(1, 13)) == 366
assert sum(days_in_month(1988, month) for month in xrange(1, 13)) == 366

# How many days have passed since 1900-01-01?
def days_after_19000101(year, month, day):
  # Check date is valid.
  assert year >= 1900
  assert month > 0
  assert month <= 12
  assert day > 0
  assert day <= days_in_month(year, month)
  year_days = sum(days_in_year(year_i) for year_i in xrange(1900, year))
  month_days = sum(days_in_month(year, month_i) for month_i in xrange(1, month))
  day_days = day - 1
  return year_days + month_days + day_days

assert days_after_19000101(1900, 1, 1) == 0
# Month of January contains 31 days.
assert days_after_19000101(1900, 2, 1) == 31
  
# Use 0-index based numbering system for weekdays.
# Monday is 0, etc.
def weekday(year, month, day):
  days = days_after_19000101(year, month, day)
  # 1900-01-01 is a Monday.
  days_in_week = 7
  return days % days_in_week

assert weekday(1900, 1, 1) == 0
assert weekday(1900, 1, 8) == 0
assert weekday(1900, 1, 7) == 6

t0 = time.time()

# Sunday = 6
result = sum(weekday(year, month, 1) == 6
             for year in xrange(1901, 2001)
             for month in xrange(1, 13))

t1 = time.time()

print(result)
print('time %f' % (t1 - t0))
# 171
# time 0.023861
# Is it faster if I accumulate days as I go?
t0 = time.time()

days = 0
for month in xrange(1, 13):
  days += days_in_month(1900, month)

sundays = 0
for year in xrange(1901, 2001):
  for month in xrange(1, 13):
    if days % 7 == 6:
      sundays += 1
    days += days_in_month(year, month)

t1 = time.time()

print(sundays)
print('time %f' % (t1 - t0))
# 171
# time 0.000549

# Yes, it is much faster if I accumulate days as I go, instead of repeatedly
# summing days.  However it is less readable.
